# magick wallpapers/1bulbasaur.jpg[1x1+0+0] -format "rgb(%[fx:round(255*u.r)],%[fx:round(255*u.g)],%[fx:round(255*u.b)])" info:
# convert wallpapers/1bulbasaur.jpg -resize 1600x2904 -background 'rgb(145,201,190)' -gravity Center -extent 1600x2904 phone-wallpapers/1bulbasaur.jpg

from os import scandir
import subprocess

input_path = 'wallpapers'
output_path = 'phone-wallpapers'
magick_rgb_template = 'magick {}/{}[1x1+0+0] -format \"rgb(%[fx:round(255*u.r)],%[fx:round(255*u.g)],%[fx:round(255*u.b)])\" info:'
convert_template = 'convert {}/{} -resize 1600x2904 -background {} -gravity Center -extent 1600x2904 {}/{}'

total_count = 0
for entry in scandir(input_path):
	if entry.path.endswith(".jpg") and entry.is_file():
		total_count = total_count + 1

counter = 1
for entry in scandir(input_path):
	if entry.path.endswith(".jpg") and entry.is_file():
		name = entry.name
		magick_rgb = magick_rgb_template.format(input_path, name).split()
		rgb = subprocess.run(magick_rgb, stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\"')
		convert = convert_template.format(input_path, name, rgb, output_path, name).split()
		subprocess.run(convert)
		print("Processed {}/{}".format(counter, total_count))
		counter = counter + 1
