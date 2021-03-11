from os import scandir
import subprocess
import re
from collections import defaultdict

input_path = 'wallpapers'
convert_template = 'convert {} -resize 1x1 txt:-'
sqlite_template = 'INSERT INTO pokemon_wallpaper (id, pokemon_id, image, primary_color)\nVALUES (\"{}\", \"{}\", \"{}\", \"{}\");\n'

f = open('pokemon_wallpapers_with_megas.sql', 'w')
special_pokemon = [
    '203girafarig2.jpg',
    '809melmetal.jpg',
    '677espurr2.jpg',
    '94gengar2.jpg',
    '251celebi2.jpg',
    '233porygon2.jpg',
    '385jirachi2.jpg'
]

unsorted_dict = defaultdict(list)
counter = 1

for entry in scandir(input_path):
    if entry.path.endswith(".jpg") and entry.is_file():
        convert = convert_template.format(entry.path).split()
        values = subprocess.run(convert, stdout=subprocess.PIPE).stdout.decode('utf-8').split(' ')
        hex_value = values[7] if values else None
        if not hex_value or hex_value[0] != '#':
            raise ValueError('Invalid hex_value found {}!'.format(entry.name))

        hex_value = hex_value.replace('#', '')
        if entry.name in special_pokemon:
            pokemon_id = re.sub(r'\D', '', entry.name[:-5])
        else:
            pokemon_id = re.sub(r'\D', '', entry.name)

        pokemon_id = int(pokemon_id)
        if pokemon_id > 809:
            raise ValueError('Invalid pokemon_id found {}!'.format(entry.name))

        wallpaper_image = entry.name.replace(str(pokemon_id), '').replace('.jpg', '')
        unsorted_dict[pokemon_id].append((wallpaper_image, hex_value))
        print('Processed {} pokemon, {} items'.format(len(unsorted_dict), counter))
        counter += 1

sorted_dict = dict(sorted(unsorted_dict.items()))
counter = 1

for pokemon_id, wallpaper_list in sorted_dict.items():
    for wallpaper_image, hex_value in wallpaper_list:
        sqlite = sqlite_template.format(counter, pokemon_id, wallpaper_image, hex_value)
        print('Wrote {} values!'.format(counter))
        counter += 1
        f.write(sqlite)
