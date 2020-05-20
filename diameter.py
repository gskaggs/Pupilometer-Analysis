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

###############################################################################
from queue import Queue

def valid(coords):
    x, y = coords
    return True

def flood_fill():
    global image
    global output
    width, height = image.size

    x_lo, x_hi, y_lo, y_hi = width, 0, height, 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    start = (width//2, height//2)

    # Invariant: Each duple put in queue must be valid
    if not valid(start):
        return None

    q = Queue(maxsize = width*height)
    q.put(start)





    return (x_lo, x_hi, y_lo, y_hi)

flood_fill()



