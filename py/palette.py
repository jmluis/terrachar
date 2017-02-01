import Image

CLIP_RECT = (0, 0, 40, 55)
R, G, B = 0, 1, 2

def getHead(color):
    head = Image.open("data/Player/Head.png").crop(CLIP_RECT)
    head = colorImage(head, color)
    return head

def getEyes(color):
    eyes = Image.open("data/Player/Eyes.png").crop(CLIP_RECT)
    eyes = colorImage(eyes, color)
    return eyes

def getEyeWhites():
    return Image.open("data/Player/Eye/Whites.png").crop(CLIP_RECT)

def getHair(id, hat, color):
    path = "data/Player/Hair{0}/{1}.png".format("Alt" if hat else "", id)
    hair = Image.open(path).crop(CLIP_RECT)
    hair = colorImage(hair, color)
    return hair

def getHelmet(headslot):
    hat = Image.open("data/Armor/Head/{0}.png".format(headslot)).crop(CLIP_RECT)
    return hat

def getShirt(gender, color):
    shirt = Image.open("data/{0}/Shirt.png".format("Female" if (gender is "Female") else "Player")).crop(CLIP_RECT)
    shirt = colorImage(shirt, color)
    return shirt

def getUndershirt(gender, color):
    undershirt = Image.open("data/{0}/Shirt.png".format("Female" if (gender is "Female") else "Player")).crop(CLIP_RECT)
    undershirt = colorImage(undershirt, color)
    return undershirt

def getHands(color):
    hands = Image.open("data/Player/Hands.png").crop(CLIP_RECT)
    hands = colorImage(hands, color)
    return hands

def getBodyArmor(gender, bodyslot):
    body = Image.open("data/{0}/Body/{1}.png".format("Female" if (gender is "Female") else "Armor", bodyslot)).crop(CLIP_RECT)
    return body

def getLegs(color):
    legs = Image.open("data/Skin/Legs.png").crop(CLIP_RECT)
    legs = colorImage(legs, color)
    return legs

def getLegArmor(legslot):
    leg = Image.open("data/Armor/Legs/{0}.png".format(legslot)).crop(CLIP_RECT)
    return leg

def getPants(gender, color):
    pants = Image.open("data/{0}/Pants.png".format("Female" if (gender is "Female") else "Player")).crop(CLIP_RECT)
    pants = colorImage(pants, color)
    return pants

def getShoes(gender, color):
    shoes = Image.open("data/{0}/Shoes.png".format("Female" if (gender is "Female") else "Player")).crop(CLIP_RECT)
    shoes = colorImage(shoes, color)
    return shoes

def getItem(id, color):
    item = Image.open("data/Item/{0}.png".format(id))

    if not color:
        return item
    else:
        return colorImage(item, color)


def colorImage(img, color):
    r, g, b, a = img.split()

    r = r.point(lambda i: (i * color[R])/254)
    g = g.point(lambda g: (g * color[G])/254)
    b = b.point(lambda j: (j * color[B])/254)

    return Image.merge('RGBA', (r, g, b, a))