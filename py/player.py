import json
from palette import Palette


class Player:
    EYE_COLOR = (105, 90, 75)
    HAIR_COLOR = (215, 90, 55)
    PANTS_COLOR = (255, 230, 175)
    SHIRT_COLOR = (175, 165, 140)
    SHOE_COLOR = (160, 105, 60)
    SKIN_COLOR = (255, 125, 90)
    UNDERSHIRT_COLOR = (160, 180, 215)
    HAIR = 0
    NAME = "NULL"
    SKIN_VARIANT = 0

    PALETTE = 0

    @property
    def GENDER(self):
        return (self.SKIN_VARIANT > 3 and self.SKIN_VARIANT is not 8)

    @staticmethod
    def loadCharacter(name):
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
        char.NAME = parsed['Name']
        char.PALETTE = Palette(char)
        return char