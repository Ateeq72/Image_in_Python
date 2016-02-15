from PIL import Image
import sys

print "Image Manipulation\n"
template = raw_input("Enter the template image: ")
destination = raw_input("Enter the destination image: ")

tempImg = Image.open(template)
destImg = Image.open(destination)

tempWidth,tempHeight = tempImg.size
destWidth,destHeight = destImg.size

if tempWidth >= destWidth and tempHeight >= destHeight:
    print "Error! The template image is larger than the destination image."
    sys.exit()
else:
    print "The template image width and height: ",tempWidth,tempHeight
    print "The destination image width and height: ",destWidth,destHeight

x_loc = raw_input("Enter the X coordinate: ")
y_loc = raw_input("Enter the Y coordinate: ")

x_loc = int(x_loc)
y_loc = int(y_loc)

tempImg = tempImg.convert("RGBA")
destImg = destImg.convert("RGBA")
img = tempImg.load()

for x in range(tempWidth):
    for y in range(tempHeight):
        if img[x,y][1] > img[x,y][0] + img[x,y][2]: #<-- removes green border from image
            img[x,y] = (255,255,255,0)
        else:
            destImg.putpixel((x+x_loc,y+y_loc),tempImg.getpixel((x,y)))


destImg.show()