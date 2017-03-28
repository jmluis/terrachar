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
    def paste_img(player, img, box=None):
        if box is None:
            x, y = img.size
            width, height = player.size
            box = ((width-x)/2, (height-y)/2, (width+x)/2, (height+y)/2)
        player.paste(im=img, box=box, mask=img)

    @staticmethod
    def draw_player(player):
        player_img = Image.new('RGBA', (86, 66), (0, 0, 0, 0))
        width, height = player_img.size

        if 0 < player.WING_SLOT < 38:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_WING, slot=player.WING_SLOT)
            if tempImg is not None:
                x, y = tempImg.size
                x_off = 0
                y_off = 0

                if player.WING_SLOT is 27:
                    x_off = 4
                elif player.WING_SLOT is 5:
                    y_off = -4
                    x_off = 4

                box = ((width - x) / 2 - 9 + x_off,  # Left
                       (height - y) / 2 + 2 + y_off, # Upper
                       (width + x) / 2 - 9 + x_off,  # Right
                       (height + y) / 2 + 2 + y_off) # Lower
                Palette.paste_img(player=player_img, box=box, img=tempImg)

        hands = None
        headpieceBeforeHair = None
        alternativeHairs = None
        sleeves = None

        # Here we draw the head-piece before the hair
        if player.HEAD_SLOT is 10 or player.HEAD_SLOT is 12 or player.HEAD_SLOT is 28 or player.HEAD_SLOT is 62 or\
            player.HEAD_SLOT is 97 or player.HEAD_SLOT is 106 or player.HEAD_SLOT is 113 or player.HEAD_SLOT is 116 or\
            player.HEAD_SLOT is 119 or player.HEAD_SLOT is 133 or player.HEAD_SLOT is 138 or player.HEAD_SLOT is 139 or\
            player.HEAD_SLOT is 163 or player.HEAD_SLOT is 178 or player.HEAD_SLOT is 181 or player.HEAD_SLOT is 191 or\
                player.HEAD_SLOT is 198:
            headpieceBeforeHair = True
        if player.HEAD_SLOT is 161 or player.HEAD_SLOT is 14 or player.HEAD_SLOT is 15 or player.HEAD_SLOT is 16 or\
            player.HEAD_SLOT is 18 or player.HEAD_SLOT is 21 or player.HEAD_SLOT is 24 or player.HEAD_SLOT is 25 or\
            player.HEAD_SLOT is 26 or player.HEAD_SLOT is 40 or player.HEAD_SLOT is 44 or player.HEAD_SLOT is 51 or\
            player.HEAD_SLOT is 56 or player.HEAD_SLOT is 59 or player.HEAD_SLOT is 60 or player.HEAD_SLOT is 67 or\
            player.HEAD_SLOT is 68 or player.HEAD_SLOT is 69 or player.HEAD_SLOT is 114 or player.HEAD_SLOT is 121 or\
            player.HEAD_SLOT is 126 or player.HEAD_SLOT is 130 or player.HEAD_SLOT is 136 or player.HEAD_SLOT is 140 or\
            player.HEAD_SLOT is 145 or player.HEAD_SLOT is 158 or player.HEAD_SLOT is 159 or player.HEAD_SLOT is 184 or\
                player.HEAD_SLOT is 190 or player.HEAD_SLOT is 92 or player.HEAD_SLOT is 195:
            alternativeHairs = True

        # __BODY STUFF __
        # let me see those hands
        if player.BODY_SLOT is 77 or player.BODY_SLOT is 103 or player.BODY_SLOT is 41 or player.BODY_SLOT is 100 or\
            player.BODY_SLOT is 10 or player.BODY_SLOT is 11 or player.BODY_SLOT is 12 or player.BODY_SLOT is 13 or\
            player.BODY_SLOT is 14 or player.BODY_SLOT is 43 or player.BODY_SLOT is 15 or player.BODY_SLOT is 16 or\
            player.BODY_SLOT is 20 or player.BODY_SLOT is 39 or player.BODY_SLOT is 50 or player.BODY_SLOT is 38 or\
            player.BODY_SLOT is 40 or player.BODY_SLOT is 57 or player.BODY_SLOT is 44 or player.BODY_SLOT is 52 or\
            player.BODY_SLOT is 53 or player.BODY_SLOT is 68 or player.BODY_SLOT is 81 or player.BODY_SLOT is 85 or\
            player.BODY_SLOT is 88 or player.BODY_SLOT is 98 or player.BODY_SLOT is 86 or player.BODY_SLOT is 87 or\
            player.BODY_SLOT is 99 or player.BODY_SLOT is 165 or player.BODY_SLOT is 166 or player.BODY_SLOT is 167 or\
            player.BODY_SLOT is 171 or player.BODY_SLOT is 45 or player.BODY_SLOT is 168 or player.BODY_SLOT is 169 or\
            player.BODY_SLOT is 42 or player.BODY_SLOT is 180 or player.BODY_SLOT is 181 or player.BODY_SLOT is 183 or\
            player.BODY_SLOT is 186 or player.BODY_SLOT is 187 or player.BODY_SLOT is 188 or player.BODY_SLOT is 64 or\
            player.BODY_SLOT is 189 or player.BODY_SLOT is 191 or player.BODY_SLOT is 192 or player.BODY_SLOT is 198 or\
                player.BODY_SLOT is 199 or player.BODY_SLOT is 202 or player.BODY_SLOT is 203:
            hands = True # draw 5
        # let me see those shoulders
        if player.BODY_SLOT is 99 or player.BODY_SLOT is 98 or player.BODY_SLOT is 100 or player.BODY_SLOT is 167 or\
            player.BODY_SLOT is 171 or player.BODY_SLOT is 183 or player.BODY_SLOT is 191 or player.BODY_SLOT is 192 or\
            player.BODY_SLOT is 198 or player.BODY_SLOT is 199 or player.BODY_SLOT is 202 or player.BODY_SLOT is 201 or\
                player.BODY_SLOT is 203:
            sleeves = True # draw 7

        # we need to draw backs
        if player.BACK_SLOT < 14 and player.BACK_SLOT > 0:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_BACK, slot=player.BACK_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

        # we need to draw body
        if player.BODY_SLOT not in [83, 82, 93]:
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.FULL_BOD, color=player.SKIN_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

            # we need to draw legs
            if player.LEGS_SLOT is not 67 and player.LEGS_SLOT is not 106\
                    and (player.LEGS_SLOT is not 140 and player.LEGS_SLOT is not 138)\
                    and (player.SHOE_SLOT is not 15 and player.LEGS_SLOT is not 143):
                tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.LEGS, color=player.SKIN_COLOR)
                Palette.paste_img(player=player_img, img=tempImg)

        # line 25918
        # do we have leg armor?
        if 0 < player.LEGS_SLOT < 157:
            tempImg = Palette.fetch_armor(gender=player.GENDER, id=PIECE_IDS.SLOT_LEGS, slot=player.LEGS_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        else:
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.PANTS, color=player.PANTS_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.SHOES, color=player.SHOE_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
        # draw shoes
        if 0 < player.SHOE_SLOT < 18:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_SHOE, slot=player.SHOE_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        # draw 14
        if player.SKIN_VARIANT in [3, 9, 7] and (player.BODY_SLOT < 1 or player.BODY_SLOT > 207 or player.BODY_SLOT is None):
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.ACCESSORIES_2, color=player.SHIRT_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

        # we need to draw body armor
        if 0 < player.BODY_SLOT < 208:
            tempImg = Palette.fetch_armor(gender=player.GENDER,id=PIECE_IDS.SLOT_BODY, slot=player.BODY_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
            if hands is True:
                tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.HANDS, color=player.SKIN_COLOR)
                Palette.paste_img(player=player_img, img=tempImg)
        else:
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.UNDERSHIRT, color=player.UNDERSHIRT_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.SHIRT, color=player.SHIRT_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.HANDS, color=player.SKIN_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

        if 0 < player.HAND_OFF_SLOT < 12:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_HANDOFF, slot=player.HAND_OFF_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        if 0 < player.WAIST_SLOT < 13:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_WAIST, slot=player.WAIST_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        if 0 < player.NECK_SLOT < 10:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_NECK, slot=player.NECK_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

        # __ HEAD STUFF __
        # if we're not wearing space creature mask or werewolf or something crazy
        if player.HEAD_SLOT is not 38 and player.HEAD_SLOT is not 135:
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.HEAD, color=player.SKIN_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.EYE_WHITES)
            Palette.paste_img(player=player_img, img=tempImg)

            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.EYES, color=player.EYE_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

        if headpieceBeforeHair is True:
            tempImg = Palette.fetch_armor(gender=player.GENDER, id=PIECE_IDS.SLOT_HEAD, slot=player.HEAD_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

            tempImg = Palette.fetch_hair(id=player.HAIR, color=player.HAIR_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
        elif alternativeHairs is True:
            tempImg = Palette.fetch_hair(id=player.HAIR, color=player.HAIR_COLOR, hat=alternativeHairs)
            Palette.paste_img(player=player_img, img=tempImg)

        if player.HEAD_SLOT is 23:
            tempImg = Palette.fetch_hair(id=player.HAIR, color=player.HAIR_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

            tempImg = Palette.fetch_armor(gender=player.GENDER, id=PIECE_IDS.SLOT_HEAD, slot=player.HEAD_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        elif (0 < player.HEAD_SLOT < 214) and player.HEAD_SLOT not in [28, 38, 39]:
            tempImg = Palette.fetch_armor(gender=player.GENDER, id=PIECE_IDS.SLOT_HEAD, slot=player.HEAD_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        elif player.FACE_SLOT not in [2, 3, 4]:
            tempImg = Palette.fetch_hair(id=player.HAIR, color=player.HAIR_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

        if 0 < player.FACE_SLOT < 9:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_FACE, slot=player.FACE_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)
        if 0 < player.SHIELD_SLOT < 7:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_SHIELD, slot=player.SHIELD_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

        # now we draw armor arms
        if 0 < player.BODY_SLOT < 208:
            if player.BODY_SLOT not in [21, 22]:
                if hands is True:
                    if sleeves is True:
                        tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.FULL_ARM, color=player.SKIN_COLOR)
                        Palette.paste_img(player=player_img, img=tempImg)
                    tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.ONE_HAND, color=player.SKIN_COLOR)
                    Palette.paste_img(player=player_img, img=tempImg)
                tempImg = Palette.fetch_armor(gender=player.GENDER, id=PIECE_IDS.SLOT_ARMS, slot=player.BODY_SLOT)
                Palette.paste_img(player=player_img, img=tempImg)
        else:
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.FULL_ARM, color=player.SKIN_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.SLEEVE, color=player.SHIRT_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)
            tempImg = Palette.fetch_piece(skin_variant=player.SKIN_VARIANT, id=PIECE_IDS.ACCESSORIES_1, color=player.SHIRT_COLOR)
            Palette.paste_img(player=player_img, img=tempImg)

        if 0 < player.HAND_ON_SLOT < 20:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_HANDON, slot=player.HAND_ON_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

        if 0 < player.FRONT_SLOT < 5:
            tempImg = Palette.fetch_accessory(id=PIECE_IDS.SLOT_FRONT, slot=player.FRONT_SLOT)
            Palette.paste_img(player=player_img, img=tempImg)

        return player_img


    @staticmethod
    def fetch_piece(skin_variant, id, color=None):
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
        return  img if color is None else Palette.color_image(img=img, color=color)

    @staticmethod
    def fetch_hair(id, color, hat=None):
        try:
            path = "data/Player/Hair{0}/{1}.png".format("" if hat is None else "Alt", (id + 1))
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
            elif id is PIECE_IDS.SLOT_WING:
                temp = Image.open("data/Wings/{0}.png".format(slot))
                width, height = temp.size
                if slot in [22, 28, 33, 34]: # {Hoverboard, Jimm's Wings, Lazure's Wings} : Only shows on Y movement
                    return None
                else:
                    crop_rect = (0, 0, width, height / 4)
                acc = temp.crop(crop_rect)
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
