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