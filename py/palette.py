from PIL import Image
import flask_app

CLIP_RECT = (0, 0, 40, 55)
R, G, B, A = 0, 1, 2, 3


class PIECE_IDS(object):
    # BASE BODY (Player/ SKINVAR / PIECEID)
    HEAD = 0  # SKIN_COLOR
    EYE_WHITES = 1  #
    EYES = 2  # EYE_COLOR
    FULL_BOD = 3  # SKIN_COLOR
    UNDERSHIRT = 4  # UNDERSHIRT_COLOR
    HANDS = 5  # SKIN_COLOR
    SHIRT = 6  # SHIRT_COLOR
    FULL_ARM = 7  # SKIN_COLOR
    SLEEVE = 8  # SHIRT_COLOR
    ONE_HAND = 9  # SKIN_COLOR
    LEGS = 10  # SKIN_COLOR
    PANTS = 11  # PANTS_COLOR
    SHOES = 12  # SHOE_COLOR
    ACCESSORIES_1 = 13  # SHIRT_COLOR
    ACCESSORIES_2 = 14  # SHIRT_COLOR
    # HAIR (Hair[Alt]/ ID )
    HAIR = 20  # HAIR_COLOR

    # ARMOR (Armor/  TYPE / SLOTID
    SLOT_HEAD = 21
    SLOT_BODY = 22
    SLOT_LEGS = 23
    SLOT_ARMS = 35

    # ACCESSORY (Acc/ TYPE  / SLOTID
    SLOT_HANDON = 24
    SLOT_HANDOFF = 25
    SLOT_BACK = 26
    SLOT_FRONT = 27
    SLOT_SHOE = 28
    SLOT_WAIST = 29
    SLOT_SHIELD = 31
    SLOT_NECK = 32
    SLOT_FACE = 33
    SLOT_BALLOON = 34

    # WING(?)  (Wings/  SLOTID  )
    SLOT_WING = 30


class Palette:
    @staticmethod
    def load_pieces(player):
        PIECES = [None] * 35
        img = None
        for i in range(0, 35):
            if (i is PIECE_IDS.HEAD or i is PIECE_IDS.FULL_BOD or i is PIECE_IDS.HANDS or i is PIECE_IDS.FULL_ARM or
                        i is PIECE_IDS.ONE_HAND or i is PIECE_IDS.LEGS):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.SKIN_COLOR)
            elif (i is PIECE_IDS.EYES):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.EYE_COLOR)
            elif (i is PIECE_IDS.EYE_WHITES):
                img = Palette._fetch_piece(skin_variant=player.SKIN_VARIANT, id=i)
            elif (i is PIECE_IDS.UNDERSHIRT or i is PIECE_IDS.SLEEVE):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.UNDERSHIRT_COLOR)
            elif (i is PIECE_IDS.SHIRT or i is PIECE_IDS.ACCESSORIES_1 or i is PIECE_IDS.ACCESSORIES_2):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.SHIRT_COLOR)
            elif (i is PIECE_IDS.PANTS):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.PANTS_COLOR)
            elif (i is PIECE_IDS.SHOES):
                img = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=i, color=player.SHOE_COLOR)
            elif (i is PIECE_IDS.HAIR):
                img = Palette.fetch_hair(id=player.HAIR, hat=(player.HEAD_SLOT is not None), color=player.HAIR_COLOR)
            # ARMOR
            elif (i is PIECE_IDS.SLOT_HEAD and (player.HEAD_SLOT is not None and player.HEAD_SLOT is not -1)):
                img = Palette.fetch_armor(gender=player.GENDER, id=i, slot=player.HEAD_SLOT)
            elif (i is PIECE_IDS.SLOT_BODY and (player.BODY_SLOT is not None and player.BODY_SLOT is not -1)):
                img = Palette.fetch_armor(gender=player.GENDER, id=i, slot=player.BODY_SLOT)
            elif (i is PIECE_IDS.SLOT_LEGS and (player.LEGS_SLOT is not None and player.LEGS_SLOT is not -1)):
                img = Palette.fetch_armor(gender=player.GENDER, id=i, slot=player.LEGS_SLOT)
            elif (i is PIECE_IDS.SLOT_ARMS and (player.BODY_SLOT is not None and player.BODY_SLOT is not -1)):
                img = Palette.fetch_armor(gender=player.GENDER, id=i, slot=player.BODY_SLOT)
            # Accessories
            elif (i is PIECE_IDS.SLOT_HANDON and (player.HAND_ON_SLOT is not None and player.HAND_ON_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.HAND_ON_SLOT)
            elif (i is PIECE_IDS.SLOT_HANDOFF and (
                            player.HAND_OFF_SLOT is not None and player.HAND_OFF_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.HAND_OFF_SLOT)
            elif (i is PIECE_IDS.SLOT_BACK and (player.BACK_SLOT is not None and player.BACK_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.BACK_SLOT)
            elif (i is PIECE_IDS.SLOT_FRONT and (player.FRONT_SLOT is not None and player.FRONT_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.FRONT_SLOT)
            elif (i is PIECE_IDS.SLOT_SHOE and (player.SHOE_SLOT is not None and player.SHOE_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.SHOE_SLOT)
            elif (i is PIECE_IDS.SLOT_WAIST and (player.WAIST_SLOT is not None and player.WAIST_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.WAIST_SLOT)
            elif (i is PIECE_IDS.SLOT_SHIELD and (player.SHIELD_SLOT is not None and player.SHIELD_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.SHIELD_SLOT)
            elif (i is PIECE_IDS.SLOT_NECK and (player.NECK_SLOT is not None and player.NECK_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.NECK_SLOT)
            elif (i is PIECE_IDS.SLOT_FACE and (player.FACE_SLOT is not None and player.FACE_SLOT is not -1)):
                img = Palette.fetch_accessory(id=i, slot=player.FACE_SLOT)
                # elif (i is PIECE_IDS.SLOT_BALLOON and (player.BALLOON_SLOT is not None and player.BALLOON_SLOT is not -1)):
                # img = Palette.fetch_accessory(id=i, slot=player.BALLOON_SLOT)
                # elif (i is PIECE_IDS.SLOT_WING and (player.WING_SLOT is not None and player.WING_SLOT is not -1)):
                # img = Palette.fetch_accessory(id=i, slot=player.WING_SLOT)
            PIECES[i] = img
        return PIECES

    @staticmethod
    def _fetch_piece(skin_variant, id):
        # lets see if the skinvar has an image
        try:
            img = Image.open("data/Player/{0}/{1}.png".format(skin_variant, id)).crop(CLIP_RECT)
        # lets grab the general gender one
        except IOError:
            try:
                img = Image.open("data/Player/{0}/{1}.png".format(
                    '4' if (skin_variant > 3 and skin_variant is not 8) else '0', id)).crop(CLIP_RECT)
            # well if that didn't have it either..
            except IOError:
                try:
                    img = Image.open("data/Player/0/{0}.png".format(id)).crop(CLIP_RECT)
                except IOError:
                    # not having an image here is fairly regular
                    if (id != PIECE_IDS.ACCESSORIES_1 and id != PIECE_IDS.ACCESSORIES_2):
                        flask_app.app.logger.warning('IOError _fetch_piece(%d : %d)', skin_variant, id)
                    return None
        return img

    @staticmethod
    def fetch_piece(skin_variant, id, color):
        return Palette.color_image(img=Palette._fetch_piece(skin_variant, id), color=color)

    @staticmethod
    def fetch_hair(id, hat, color):
        try:
            path = "data/Player/Hair{0}/{1}.png".format("Alt" if hat else "", (id + 1))
            hair = Image.open(path).crop(CLIP_RECT)
            hair = Palette.color_image(hair, color)
        except IOError:
            flask_app.app.logger.warning('IOError fetch_hair (%d)', id)
            return None
        return hair

    @staticmethod
    def fetch_armor(gender, id, slot):
        try:
            if id is PIECE_IDS.SLOT_HEAD:
                armor = Image.open("data/Armor/Head/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_BODY:
                armor = Image.open("data/{0}/Body/{1}.png".format("Female" if gender else "Armor", slot)).crop(
                    CLIP_RECT)
            elif id is PIECE_IDS.SLOT_LEGS:
                armor = Image.open("data/Armor/Legs/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_ARMS:
                armor = Image.open("data/Armor/Arm/{0}.png".format(slot)).crop(CLIP_RECT)
            else:
                return None
        except IOError as e:
            flask_app.app.logger.warning('IOError fetch_armor (%d : %d : %d)', gender, id, slot)
            return None

        return armor

    @staticmethod
    def fetch_accessory(id, slot):
        try:
            if id is PIECE_IDS.SLOT_HANDON:  # cool
                acc = Image.open("data/Acc/HandsOn/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_HANDOFF:  # cool
                acc = Image.open("data/Acc/HandsOff/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_BACK:  # cool
                acc = Image.open("data/Acc/Back/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_FRONT:  # cool
                acc = Image.open("data/Acc/Front/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_SHOE:  # cool
                acc = Image.open("data/Acc/Shoes/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_WAIST:  # ok 40/1064
                acc = Image.open("data/Acc/Waist/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_SHIELD:  # cool
                acc = Image.open("data/Acc/Shield/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_NECK:  # cool
                acc = Image.open("data/Acc/Neck/{0}.png".format(slot)).crop(CLIP_RECT)
            elif id is PIECE_IDS.SLOT_FACE:  # cool
                acc = Image.open("data/Acc/Face/{0}.png".format(slot)).crop(CLIP_RECT)
                # elif id is PIECE_IDS.SLOT_BALLOON: # no
                # acc = Image.open("data/Acc/Balloon/{0}.png".format(slot)).crop((0,0,52,56)? [TODO])
                # elif id is PIECE_IDS.SLOT_WING: # no
                # acc = Image.open("data/Wings/{0}.png".format(slot)).crop([TODO])
            else:
                return None
        except IOError:
            flask_app.app.logger.warning('IOError fetch_accessory (%d : %d)', id, slot)
            return None
        return acc

    @staticmethod
    def fetch_item(id, color):
        try:
            item = Image.open("data/Item/{0}.png".format(id))
            if not color:
                return item
            else:
                return Palette.color_image(item, color)
        except IOError:
            flask_app.app.logger.warning('IOError fetch_item (%d : %d)', id)
            return None

    @staticmethod
    def color_image(img, color):
        if img is None:
            return None
        r, g, b, a = img.split()

        r = r.point(lambda i: (i * color[R]) / 254)
        g = g.point(lambda g: (g * color[G]) / 254)
        b = b.point(lambda j: (j * color[B]) / 254)

        return Image.merge('RGBA', (r, g, b, a))
