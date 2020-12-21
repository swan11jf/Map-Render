import os
from PIL import Image

rootdir = r'C:\Users\Jeremy Feng\Desktop\Python Projects\Map Project\trial'

pathnames = []
directories = []
image_list = []
image_list2 = []
coordinates = []

for root, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
        name = file[:-4]

        if name[1:3] == '03':
            x = 0
        else:
            x = 1

        if name[-1:] == 'F':
            y = 0
        elif name[-1:] == 'G':
            y = 1
        else:
            y = 2

        coordinates.append((x,y))

        pathname = os.path.join(rootdir, file)
        pathnames.append(pathname)

for pathname in pathnames:
    im = Image.open(pathname)
    image_list.append(im)

def stitch(background, im, n, x, y):
    background.paste(im, (x*n, y*n))
    return background

n = 4000

background = Image.new('RGB', (2*n, 3*n))
print(coordinates)

print(coordinates[1][0])

for i in range(len(image_list)):
    x = coordinates[i][0]
    y = coordinates[i][1]

    output = stitch(background, image_list[i], n, x, y)

output.save("complete.jpg")