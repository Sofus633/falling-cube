import pyxel

#10 x 10 cube

class Cube:
    def __init__(self, position):
        # [[y, x], [y,x]]
        #  top      bottom
        self.position = [position, [position[0] + 10, position[1] + 10]]
        self.state = 'moving'
        
    def update(self):
        print(self.state, self.position)
        self.checkbottom()
        if self.position[1][0] >= 160:
            self.state = 'freeze'
            
        if self.state == 'moving':
            self.position[0][0] += 5
            self.position[1][0] += 5
            print("moving")
    def checkbottom(self):
        if pyxel.pget(self.position[0][0] + 1, self.position[0][1] + 1) == 5 or pyxel.pget(self.position[1][0] - 1, self.position[1][1] - 1) == 5:
            self.state = 'freeze'
        else:
            self.state = 'moving'
