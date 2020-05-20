from PIL import Image

command_line = input().split()
command_line_names = ["Photo Name", "Pixel Width (mm)", "Epsilon"]
for arg in zip(command_line_names, command_line):
    print(arg)

filename = command_line[0]
pxl_width = float(command_line[1])
epsilon = float(command_line[2])

image = Image.open(filename)
in_data = image.load()
output = image.copy()
out_data = output.load()


###############################################################################
from queue import Queue

def intensity(color):
    return (color[0]**2 + color[1]**2 + color[2]**2)**0.5

def valid(x, y):
    global epsilon
    global image
    width, height = image.size
    global in_data

    # In Bounds
    if x < 0 or y < 0 or x >= width or y >= height:
        return False

    return intensity(in_data[x,y]) < epsilon


def flood_fill():
    global image
    global output
    global out_data
    width, height = image.size

    x_lo, x_hi, y_lo, y_hi = width, 0, height, 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited = [[False for y in range(height)] for x in range(width)]

    start = (width//2, height//2)

    # Invariant: Each duple put in queue must be valid
    if not valid(start[0], start[1]):
        return None

    q = Queue(maxsize = width*height)
    q.put(start)

    # Breadth First Search
    while not q.empty():
        x, y = q.get()
        
        if visited[x][y]:
            continue

        visited[x][y] = True

        # Update result
        x_lo = min(x_lo, x)
        x_hi = max(x_hi, x)
        y_lo = min(y_lo, y)
        y_hi = max(y_hi, y)

        for i in range(len(dx)):
            # x prime, y prime: The next coordinates to consider
            xp, yp = x + dx[i], y + dy[i]
            if valid(xp, yp):
                q.put((xp, yp))
            else:
                # Edge point
                out_data[x,y] = (0,0,255)

    return (x_lo, x_hi, y_lo, y_hi)

result = flood_fill()
#result = None
if result:
    print(result)
else:
    print("Pupil Not Centered")


output.save("out_image.png")
