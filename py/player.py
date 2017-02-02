from palette import Palette
import random


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
    HEAD_SLOT = None
    BODY_SLOT = None
    LEGS_SLOT = None
    HAND_ON_SLOT = None
    HAND_OFF_SLOT = None
    BACK_SLOT = None
    FRONT_SLOT = None
    SHOE_SLOT = None
    WAIST_SLOT = None
    WING_SLOT = None
    SHIELD_SLOT = None
    NECK_SLOT = None
    FACE_SLOT = None
    BALLOON_SLOT = None

    @property
    def GENDER(self):
        return (self.SKIN_VARIANT > 3 and self.SKIN_VARIANT is not 8)

    def load_palette(self):
        self.PALETTE = Palette.load_pieces(self)

    def randomize(self):
        self.NAME = "ID" + str(random.randint(0, 9999))
        self.SKIN_VARIANT = random.randint(0, 9)
        self.HAIR = random.randint(0, 134)
        for i in range(0, 2):
            self.EYE_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.SKIN_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.PANTS_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.SHIRT_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.HAIR_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.UNDERSHIRT_COLOR[i] = random.randint(0, 255)
        for i in range(0, 2):
            self.SHOE_COLOR[i] = random.randint(0, 255)
        self.HEAD_SLOT = random.randint(1, 213)
        self.BODY_SLOT = random.randint(1, 207)
        self.LEGS_SLOT = random.randint(1, 156)
        # self.HAND_ON_SLOT = random.randint(1,19)
        # self.HAND_OFF_SLOT = random.randint(1,11)
        # self.BACK_SLOT = random.randint(1,13)
        # self.FRONT_SLOT = random.randint(1,4)
        self.SHOE_SLOT = random.randint(1, 17)
        # self.WAIST_SLOT = random.randint(1,12)
        # self.WING_SLOT = random.randint(1,37)
        # self.SHIELD_SLOT = random.randint(1,6)
        # self.NECK_SLOT = random.randint(1,9)
        # self.FACE_SLOT = random.randint(1,8)
        # self.BALLOON_SLOT = random.randint(1,17)
        self.load_palette()

    def load_data(self, parsed):
        self.EYE_COLOR = [int(x) for x in parsed['EyeColor']]
        self.HAIR_COLOR = [int(x) for x in parsed['HairColor']]
        self.PANTS_COLOR = [int(x) for x in parsed['PantsColor']]
        self.SHIRT_COLOR = [int(x) for x in parsed['ShirtColor']]
        self.SHOE_COLOR = [int(x) for x in parsed['ShoeColor']]
        self.SKIN_COLOR = [int(x) for x in parsed['SkinColor']]
        self.UNDERSHIRT_COLOR = [int(x) for x in parsed['UnderShirtColor']]
        self.HAIR = int(parsed['Hair'])
        self.SKIN_VARIANT = int(parsed['SkinVariant'])

        if 'HeadSlot' in parsed:
            self.HEAD_SLOT = int(parsed['HeadSlot'])
        if 'BodySlot' in parsed:
            self.BODY_SLOT = int(parsed['BodySlot'])
        if 'LegsSlot' in parsed:
            self.LEGS_SLOT = int(parsed['LegsSlot'])
        if 'HandsOnSlot' in parsed:
            self.HAND_ON_SLOT = int(parsed['HandsOnSlot'])
        if 'HandsOffSlot' in parsed:
            self.HAND_OFF_SLOT = int(parsed['HandsOffSlot'])
        if 'BackSlot' in parsed:
            self.BACK_SLOT = int(parsed['BackSlot'])
        if 'FrontSlot' in parsed:
            self.FRONT_SLOT = int(parsed['FrontSlot'])
        if 'ShoeSlot' in parsed:
            self.SHOE_SLOT = int(parsed['ShoeSlot'])
        if 'WaistSlot' in parsed:
            self.WAIST_SLOT = int(parsed['WaistSlot'])
        if 'WingSlot' in parsed:
            self.WING_SLOT = int(parsed['WingSlot'])
        if 'ShieldSlot' in parsed:
            self.SHIELD_SLOT = int(parsed['ShieldSlot'])
        if 'NeckSlot' in parsed:
            self.NECK_SLOT = int(parsed['NeckSlot'])
        if 'FaceSlot' in parsed:
            self.FACE_SLOT = int(parsed['FaceSlot'])
        if 'BalloonSlot' in parsed:
            self.BALLOON_SLOT = int(parsed['BalloonSlot'])

        self.NAME = parsed['Name']
        self.load_palette()
