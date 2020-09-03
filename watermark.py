# convert originals/1bulbasaur.jpg -fill 'rgb(145,201,190)' -draw "rectangle 0,1175 600,1200" wallpapers/1bulbasaur.jpg

from os import scandir
import subprocess

input_path = 'originals'
output_path = 'wallpapers'
magick_rgb_template = 'magick {}/{}[1x1+0+0] -format \"rgb(%[fx:round(255*u.r)],%[fx:round(255*u.g)],%[fx:round(255*u.b)])\" info:'
watermark_template = 'convert {}/{} -fill {} -draw \"\" {}/{}'
rectangle = "rectangle 0,1175 600,1200"

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
		watermark = watermark_template.format(input_path, name, rgb, output_path, name).split()
		watermark[5] = rectangle
		subprocess.run(watermark)
		print("Processed {}/{}".format(counter, total_count))
		counter = counter + 1
