from os import scandir
import re

input_path = 'wallpapers'
sqlite_template = 'UPDATE pokemon SET wallpaper_images = \'{}\' WHERE id = {};\n'

dictionary = {}
for entry in scandir(input_path):
	if entry.path.endswith('.jpg') and entry.is_file():
		pokemon_id = re.sub(r'\D', '', entry.name)
		wallpaper_image = entry.name.replace(str(pokemon_id), '')
		dictionary[pokemon_id] = dictionary.get(pokemon_id, []) + [wallpaper_image]

f = open('pokemon_wallpaper_images.sql', 'w')
for id in dictionary:
	wallpaper_images = ','.join(dictionary[id])
	sqlite = sqlite_template.format(wallpaper_images, id)
	f.write(sqlite)
