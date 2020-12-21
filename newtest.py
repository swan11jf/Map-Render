import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = 516000000

rootdir = r'C:\Users\Jeremy Feng\Desktop\Python Projects\Map Project\trial'

n = 4000

pathnames = []
coordinates = []
image_list = []
xvals = []
yvals = []

def stitch(background, im, n, x, y):
    background.paste(im, (x*n, y*n))
    return background

for root, dirs, files in os.walk(rootdir):
    for file in files:
        name = file[:-4]

        y = ord(name[-1:])-65
        x = int(name[1:3])-1
        coordinates.append((x,y))

        if name[1:3] not in xvals:
            xvals.append(name[1:3])

        if name[-1:] not in yvals:
            yvals.append(name[-1:])

        pathname = os.path.join(rootdir, file)
        pathnames.append(pathname)

# yvals = [ord(yvals[i]) - 64 for i in range(len(yvals))]
# xvals = [int(xvals[i]) for i in range(len(xvals))]

ymax = max([ord(yvals[i]) - 64 for i in range(len(yvals))])
xmax = max([int(xvals[i]) for i in range(len(xvals))])

for pathname in pathnames:
    im = Image.open(pathname)
    image_list.append(im)

background = Image.new('RGB', (xmax*n, ymax*n), (0, 255, 255))

for i in range(len(image_list)):
    x = coordinates[i][0]
    y = coordinates[i][1]
    output = stitch(background, image_list[i], n, x, y)

width, height = output.size

left = 0
top = 4000*3
right = width
bottom = height

final = output.crop((left, top, right, bottom))
final.save("test.jpg")

