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
    HEAD_SLOT = -1
    BODY_SLOT = -1
    LEGS_SLOT = -1
    HAND_ON_SLOT = -1
    HAND_OFF_SLOT = -1
    BACK_SLOT = -1
    FRONT_SLOT = -1
    SHOE_SLOT = -1
    WAIST_SLOT = -1
    WING_SLOT = -1
    SHIELD_SLOT = -1
    NECK_SLOT = -1
    FACE_SLOT = -1
    BALLOON_SLOT = -1

    @property
    def GENDER(self):
        return self.SKIN_VARIANT > 3 and self.SKIN_VARIANT is not 8

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