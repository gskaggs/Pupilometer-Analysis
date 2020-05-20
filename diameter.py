from PIL import Image

command_line = input().split()
command_line_names = ["Photo Name", "Epsilon"]
for arg in zip(command_line_names, command_line):
    print(arg)

filename = command_line[0]
epsilon = float(command_line[1])







