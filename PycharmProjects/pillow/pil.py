import random
from PIL import Image
N = 4
# im = Image.open("python.jpg")
im = Image.open("me.jpg")

im_width = im.size[0] / N
im_height = im.size[1] / N

new_image = Image.new(im.mode, (im.size[0], im.size[1]))
pieces = []

for x, y in [(int(im_width * x), int(im_height * y)) for x in range(N) for y in range(N)]:
    pieces.append(im.crop((x, y, int(x + im_width), int(y + im_height))))

random.shuffle(pieces)

for i, (x, y) in enumerate([(int(im_width * x), int(im_height * y)) for x in range(N) for y in range(N)]):
    new_image.paste(pieces[i], (x, y, int(x + im_width), int(y + im_height)))


new_image.save('new.png')
