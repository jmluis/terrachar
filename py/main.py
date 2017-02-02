#!/usr/bin/env python

import Image
from player import Player
import time


def draw_character(player, image):
    for piece in player.PALETTE:
        if piece is None:
            continue
        image.paste(im=piece, mask=piece)

    return image


def main(name):
    f = open("{0}.json".format(name)).read()
    char = Player()
    char.loadData(f)

    # normal and blocky
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = draw_character(char, char_img)
    char_img.save("{0}.png".format(char.NAME), "PNG", quality=100)

    char.randomize()
    # bigger, still pixel-y
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = draw_character(char, char_img)
    char_img = char_img.resize((80, 110), Image.NEAREST)
    char_img.save("{0}.png".format(char.NAME), "PNG", quality=100)

    char.randomize()
    # smoother, way smoother
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = draw_character(char, char_img)
    char_img = char_img.resize((80, 110), Image.ANTIALIAS)
    char_img.save("{0}.png".format(char.NAME), "PNG", quality=100)

### Debugging
#    for i in range (0, 100):
#        char.randomize()
#        char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
#        char_img = drawCharacter(char, char_img)
#        char_img = char_img.resize((80, 110), Image.ANTIALIAS)
#        char_img.save("{0}.png".format(char.NAME), "PNG", quality=100)


start = time.time()
main('0')
end = time.time()
print end - start