#!/usr/bin/env python

import Image
import json
from player import Player
from palette import Palette

def drawCharacter(player, image):
    for piece in player.PALETTE:
        if piece is None:
            continue
        image.paste(im=piece, mask=piece)

    return image

def main(name):
    f = open("{0}.json".format(name)).read()
    parsed = json.loads(f)
    char = Player()
    char.EYE_COLOR = [int(x) for x in parsed['EyeColor'].split(',')]
    char.HAIR_COLOR = [int(x) for x in parsed['HairColor'].split(',')]
    char.PANTS_COLOR = [int(x) for x in parsed['PantsColor'].split(',')]
    char.SHIRT_COLOR = [int(x) for x in parsed['ShirtColor'].split(',')]
    char.SHOE_COLOR = [int(x) for x in parsed['ShoeColor'].split(',')]
    char.SKIN_COLOR = [int(x) for x in parsed['SkinColor'].split(',')]
    char.UNDERSHIRT_COLOR = [int(x) for x in parsed['UnderShirtColor'].split(',')]
    char.HAIR = int(parsed['Hair'])
    char.SKIN_VARIANT = int(parsed['SkinVariant'])
    char.HEAD_SLOT = int(parsed['HeadSlot'])
    char.BODY_SLOT = int(parsed['BodySlot'])
    char.LEGS_SLOT = int(parsed['LegsSlot'])
    char.HAND_ON_SLOT = int(parsed['HandsOnSlot'])
    char.HAND_OFF_SLOT = int(parsed['HandsOffSlot'])
    char.BACK_SLOT = int(parsed['BackSlot'])
    char.FRONT_SLOT = int(parsed['FrontSlot'])
    char.SHOE_SLOT = int(parsed['ShoeSlot'])
    char.WAIST_SLOT = int(parsed['WaistSlot'])
    char.WING_SLOT = int(parsed['WingSlot'])
    char.SHIELD_SLOT = int(parsed['ShieldSlot'])
    char.NECK_SLOT = int(parsed['NeckSlot'])
    char.FACE_SLOT = int(parsed['FaceSlot'])
    char.BALLOON_SLOT = int(parsed['BalloonSlot'])

    char.NAME = parsed['Name']
    char.PALETTE = Palette.load_pieces(char)

    char_img = Image.new('RGBA', (40, 55), (255, 255, 255, 255))
    char_img = drawCharacter(char, char_img)

    char_img.save("{0}.png".format(char.NAME), "PNG")
main('0')
