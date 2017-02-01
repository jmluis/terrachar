#!/usr/bin/env python

import Image
import palette
import json


EYE_COLOR = (105, 90, 75)
HAIR_COLOR = (215, 90, 55)
PANTS_COLOR = (255, 230, 175)
SHIRT_COLOR = (175, 165, 140)
SHOE_COLOR = (160, 105, 60)
SKIN_COLOR = (255, 125, 90)
UNDERSHIRT_COLOR = (160, 180, 215)
GENDER = "Male"
HAIR = 0 + 1
NAME = "NULL"


def loadCharacter(name):
    f = open("{0}.json".format(name)).read()
    parsed = json.loads(f)
    EYE_COLOR = [int(x) for x in parsed['EyeColor'].split(',')]
    HAIR_COLOR = [int(x) for x in parsed['HairColor'].split(',')]
    PANTS_COLOR = [int(x) for x in parsed['PantsColor'].split(',')]
    SHIRT_COLOR = [int(x) for x in parsed['ShirtColor'].split(',')]
    SHOE_COLOR = [int(x) for x in parsed['ShoeColor'].split(',')]
    SKIN_COLOR = [int(x) for x in parsed['SkinColor'].split(',')]
    UNDERSHIRT_COLOR = [int(x) for x in parsed['UnderShirtColor'].split(',')]
    HAIR = int(parsed['Hair']) + 1

    GENDER = "Female" if (int(parsed['SkinVariant']) < 4) else "Male"
    NAME = name

    char_img = Image.new('RGBA', (40,55), (255, 255, 255, 255))
    shirt = palette.getShirt(GENDER, SHIRT_COLOR)
    shoes = palette.getShoes(GENDER, SHOE_COLOR)
    pants = palette.getPants(GENDER, PANTS_COLOR)
    undershirt = palette.getUndershirt(GENDER, UNDERSHIRT_COLOR)
    hands = palette.getHands(SKIN_COLOR)
    hair = palette.getHair(HAIR, False, HAIR_COLOR)
    head = palette.getHead(SKIN_COLOR)
    eyes = palette.getEyes(EYE_COLOR)
    eyeWhites = palette.getEyeWhites()

    char_img.paste(pants, mask=pants)
    char_img.paste(shoes, mask=shoes)
    char_img.paste(shirt, mask=shirt)
    char_img.paste(undershirt, mask=undershirt)
    char_img.paste(hands, mask=hands)
    char_img.paste(head, mask=head)
    char_img.paste(eyes, mask=eyes)
    char_img.paste(eyeWhites, mask=eyeWhites)
    char_img.paste(hair, mask=hair)

    char_img.save("{0}.png".format(NAME), "PNG")

def main():
    loadCharacter('fdgh')
main()