#!/usr/bin/env python

import Image
from player import Player

def drawCharacter(player, image):
    for piece in player.PALETTE:
        if piece is None:
            continue
        image.paste(im=piece, mask=piece)

    return image

def main():
    pl = Player.loadCharacter('0')

    char_img = Image.new('RGBA', (40, 55), (255, 255, 255, 255))
    char_img = drawCharacter(pl, char_img)

    char_img.save("{0}.png".format(pl.NAME), "PNG")
main()
