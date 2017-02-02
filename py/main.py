#!/usr/bin/env python

import Image
import json
from player import Player
from palette import Palette
import random
import time


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

    # normal and blocky
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = drawCharacter(char, char_img)
    char_img.save("{0}.png".format(char.NAME), "PNG", quality=100)

    # bigger, still pixel-y
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = drawCharacter(char, char_img)
    char_img = char_img.resize((80, 110), Image.NEAREST)
    char_img.save("{0}alt.png".format(char.NAME), "PNG", quality=100)

    # smoother, way smoother
    char_img = Image.new('RGBA', (40, 55), (0, 0, 0, 0))
    char_img = drawCharacter(char, char_img)
    char_img = char_img.resize((160, 220), Image.ANTIALIAS)
    char_img = char_img.resize((80, 110), Image.NEAREST)
    char_img.save("{0}alt2.png".format(char.NAME), "PNG", quality=100)

def randy(char):
    char.HEAD_SLOT = random.randint(1,213)
    char.BODY_SLOT = random.randint(1,207)
    char.LEGS_SLOT = random.randint(1,156)
    #char.HAND_ON_SLOT = random.randint(1,19)
    #char.HAND_OFF_SLOT = random.randint(1,11)
    #char.BACK_SLOT = random.randint(1,13)
    #char.FRONT_SLOT = random.randint(1,4)
    char.SHOE_SLOT = random.randint(1,17)
    #char.WAIST_SLOT = random.randint(1,12)
    #char.WING_SLOT = random.randint(1,37)
    #char.SHIELD_SLOT = random.randint(1,6)
    #char.NECK_SLOT = random.randint(1,9)
    #char.FACE_SLOT = random.randint(1,8)
    #char.BALLOON_SLOT = random.randint(1,17)
    return char
start = time.time()
main('0')
end = time.time()
print end - start