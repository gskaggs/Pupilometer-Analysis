from PIL import Image

command_line = input().split()
command_line_names = ["Photo Name", "Pixel Width (mm)", "Epsilon"]
for arg in zip(command_line_names, command_line):
    print(arg)

filename = command_line[0]
pxl_width = float(command_line[1])
epsilon = float(command_line[2])

image = Image.open(filename)
output = image.copy()

output.save("out_image.png")




