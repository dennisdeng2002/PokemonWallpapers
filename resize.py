# convert wallpapers/1bulbasaur.jpg -resize 800 wallpapers-0.5/1bulbasaur.jpg
# convert wallpapers/1bulbasaur.jpg -resize 400 wallpapers-0.25/1bulbasaur.jpg

from os import scandir
import subprocess

input_paths = ['wallpapers', 'wallpapers', 'phone-wallpapers', 'phone-wallpapers']
output_paths = ['wallpapers-0.5', 'wallpapers-0.25', 'phone-wallpapers-0.5', 'phone-wallpapers-0.25']
widths = [800, 400, 800, 400]
resize_template = 'convert {}/{} -resize {} {}/{}'

for i, input_path in enumerate(input_paths):
    total_count = 0
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            total_count = total_count + 1

    counter = 1
    output_path, width = output_paths[i], widths[i]
    for entry in scandir(input_path):
        if entry.path.endswith('.jpg') and entry.is_file():
            name = entry.name
            resize = resize_template.format(input_path, name, width, output_path, name).split()
            subprocess.run(resize)
            print("Processed {}/{}".format(counter, total_count))
            counter = counter + 1
