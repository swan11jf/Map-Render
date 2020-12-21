import os, glob
from PIL import Image

def stitch_h(im1, im2):
    background = Image.new('RGB', (im1.width + im2.width, im1.height))
    background.paste(im1, (0,0))
    background.paste(im2, (im1.width, 0))
    return background

def stitch_v(im1, im2):
    out = Image.new('RGB', (im1.width, im1.height + im2.height))
    out.paste(im1, (0,0))
    out.paste(im2, (0,im1.height))
    return out

def stitch_hm(im_list):
    out = im_list.pop(0)
    for img in im_list:
        out = stitch_h(out, img)
    return out

def stitch_vm(im_list):
    out = im_list.pop(0)
    for img in im_list:
        out = stitch_v(out, img)
    return out

rootdir = r'C:\Users\Jeremy Feng\Desktop\Python Projects\Map Project\maps'

pathnames = []
directories = []
image_list = []
image_list2 = []

for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        pathname = os.path.join(subdir, dir)
        pathnames.append(pathname)
        directories.append(dir)

for pathname in pathnames:
    for file in glob.glob(pathname + '\\*.jpg'):
        im = Image.open(file)
        image_list.append(im)
    for i in range(0, 100, 10):
        row = stitch_hm(image_list[i:i + 10])
        image_list2.append(row)
    stitch_vm(image_list2).save("complete\\" + directories[pathnames.index(pathname)] + '.jpg')

    image_list.clear()
    image_list2.clear()

