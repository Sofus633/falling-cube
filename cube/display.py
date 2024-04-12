
def draw(objecttodraw):
    if type(objecttodraw) == Cube:
        pyxle.rect(objecttodraw.position[0][1], objecttodraw.position[0][0], 10, 10, 1)

