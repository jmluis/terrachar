import Image

CLIP_RECT = (0, 0, 40, 55)
R, G, B = 0, 1, 2

class Palette:
    def __init__(self, player):
        self.shirt = self.getShirt(player.GENDER, player.SHIRT_COLOR)
        self.shoes = self.getShoes(player.GENDER, player.SHOE_COLOR)
        self.pants = self.getPants(player.GENDER, player.PANTS_COLOR)
        self.undershirt = self.getUndershirt(player.GENDER, player.UNDERSHIRT_COLOR)
        self.hands = self.getHands(player.SKIN_COLOR)
        self.hair = self.getHair(player.HAIR, False, player.HAIR_COLOR)
        self.head = self.getHead(player.SKIN_COLOR)
        self.eyes = self.getEyes(player.EYE_COLOR)
        self.eyeWhites = self.getEyeWhites()
    @staticmethod
    def getHead(color):
        head = Image.open("data/Player/Head.png").crop(CLIP_RECT)
        head = Palette.colorImage(head, color)
        return head

    @staticmethod
    def getEyes(color):
        eyes = Image.open("data/Player/Eyes.png").crop(CLIP_RECT)
        eyes = Palette.colorImage(eyes, color)
        return eyes

    @staticmethod
    def getEyeWhites():
        return Image.open("data/Player/Eye/Whites.png").crop(CLIP_RECT)

    @staticmethod
    def getHair(id, hat, color):
        path = "data/Player/Hair{0}/{1}.png".format("Alt" if hat else "", (id + 1))
        hair = Image.open(path).crop(CLIP_RECT)
        hair = Palette.colorImage(hair, color)
        return hair

    @staticmethod
    def getShirt(gender, color):
        shirt = Image.open("data/{0}/Shirt.png".format("Female" if gender else "Player")).crop(CLIP_RECT)
        shirt = Palette.colorImage(shirt, color)
        return shirt

    @staticmethod
    def getUndershirt(gender, color):
        undershirt = Image.open("data/{0}/Undershirt.png".format("Female" if gender else "Player")).crop(CLIP_RECT)
        undershirt = Palette.colorImage(undershirt, color)
        return undershirt

    @staticmethod
    def getHands(color):
        hands = Image.open("data/Player/Hands.png").crop(CLIP_RECT)
        hands = Palette.colorImage(hands, color)
        return hands

    @staticmethod
    def getLegs(color):
        legs = Image.open("data/Skin/Legs.png").crop(CLIP_RECT)
        legs = Palette.colorImage(legs, color)
        return legs

    @staticmethod
    def getPants(gender, color):
        pants = Image.open("data/{0}/Pants.png".format("Female" if gender else "Player")).crop(CLIP_RECT)
        pants = Palette.colorImage(pants, color)
        return pants

    @staticmethod
    def getShoes(gender, color):
        shoes = Image.open("data/{0}/Shoes.png".format("Female" if gender else "Player")).crop(CLIP_RECT)
        shoes = Palette.colorImage(shoes, color)
        return shoes

    # todo
    @staticmethod
    def getHelmet(headslot):
        hat = Image.open("data/Armor/Head/{0}.png".format(headslot)).crop(CLIP_RECT)
        return hat

    @staticmethod
    def getBodyArmor(gender, bodyslot):
        body = Image.open("data/{0}/Body/{1}.png".format("Female" if gender else "Armor", bodyslot)).crop(CLIP_RECT)
        return body

    @staticmethod
    def getLegArmor(legslot):
        leg = Image.open("data/Armor/Legs/{0}.png".format(legslot)).crop(CLIP_RECT)
        return leg

    @staticmethod
    def getItem(id, color):
        item = Image.open("data/Item/{0}.png".format(id))

        if not color:
            return item
        else:
            return Palette.colorImage(item, color)

    @staticmethod
    def colorImage(img, color):
        r, g, b, a = img.split()

        r = r.point(lambda i: (i * color[R])/254)
        g = g.point(lambda g: (g * color[G])/254)
        b = b.point(lambda j: (j * color[B])/254)

        return Image.merge('RGBA', (r, g, b, a))