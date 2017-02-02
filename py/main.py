#!/usr/bin/env python

import Image
from player import Player


def drawCharacter(player, image):
    image.paste(player.PALETTE.pants, mask=player.PALETTE.pants)
    image.paste(player.PALETTE.shoes, mask=player.PALETTE.shoes)
    image.paste(player.PALETTE.shirt, mask=player.PALETTE.shirt)
    image.paste(player.PALETTE.undershirt, mask=player.PALETTE.undershirt)
    image.paste(player.PALETTE.hands, mask=player.PALETTE.hands)
    image.paste(player.PALETTE.head, mask=player.PALETTE.head)
    image.paste(player.PALETTE.eyes, mask=player.PALETTE.eyes)
    image.paste(player.PALETTE.eyeWhites, mask=player.PALETTE.eyeWhites)
    image.paste(player.PALETTE.hair, mask=player.PALETTE.hair)
    return image

def main():
    pl = Player.loadCharacter('fdgh')

    char_img = Image.new('RGBA', (40, 55), (255, 255, 255, 255))
    char_img = drawCharacter(pl, char_img)

    char_img.save("{0}.png".format(pl.NAME), "PNG")
main()