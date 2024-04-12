import pyxel
from cube import Cube
#from display import draw

class ObjectList:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def delete_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            print("Object not found in the list.")

class App:
    def __init__(self):
        self.click = False
        self.ToUpdate = ObjectList()
        self.listofcubes = ObjectList()
        cube1 = Cube([1, 0])
        self.listofcubes.add_object(cube1)
        
        self.grabed = None
        
        pyxel.init(160, 160, title="SuperUltraMegaGame")
        pyxel.load("wow.pyxres")
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pyxel.cls(1)
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        mousepos = (y, x)
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and not self.click:
            #res = check_collition(mousepos, self.listofcubes)
            #if res[0]:
            #   self.grabed = res[1] 
            #   self.click = True
            self.listofcubes.add_object(Cube([y, x]))
            
        if not pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.click:
            self.click = False
            self.grabed = None
        
        
        for cube in self.listofcubes.objects:
            cube.update()

        
        
    def draw(self):
        for cube in self.listofcubes.objects:
            drawa(cube)
    
def check_collition(object1, object2):
    
    # [[x, y], [w, h]]
    obj1_upc = object1
    obj1_downc = object1

    objectcoslide = []
    
    for obj in object2.objects:
        obj2_upc = obj.position[0]
        print(obj.position)
        obj2_downc = [obj.position[0][0] + obj.position[1][0], obj.position[0][1] + obj.position[1][1]]
        if obj1_upc[0] < obj2_upc[0] and obj2_upc[0] < obj1_downc[0] and obj1_upc[1] < obj2_upc[1] and obj2_upc[1] < obj1_downc[1]:
            objectcolide.append(obj)
            
    if len(objectcoslide) > 0:
        return [True, objectcoslide[0]]
    else:
        return [False, None]


def drawa(objecttodraw):
    if type(objecttodraw) == Cube:
        print(objecttodraw.position)
        pyxel.rect(objecttodraw.position[0][1], objecttodraw.position[0][0], 10, 10, 5)


App()
        
        
