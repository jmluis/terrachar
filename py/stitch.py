import glob
from PIL import Image


def do_stitch(pictures):
    images = map(Image.open, pictures)
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save('test.png')

to_stitch = glob.glob('*.png')
do_stitch(to_stitch)