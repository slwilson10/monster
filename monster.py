import sys
import random

class Grid:
    def __init__(self, maxH, maxW):
        self.max_height = maxH
        self.max_width = maxW
        
    def grid_size(self):
        return [self.max_height, self.max_width]
            

class Character:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        
    def position(self):
        return [self.positionX, self.positionY]  

class Player(Character):
    pass
    # def __init__(self, posX, posY):
        # Character.__init__(self, posX, posY) 
    def place(self):
        self.position = [random.randint(0,Grid_Size()[0] - 1),random.randint(0,Grid_Size()[1] - 1))]    

class Monster(Character):
    pass

class Item:
    pass

class Treasure(Item):
    pass

class Trap(Item):
    pass

class Exit(Item):
    pass

    
def setup_game():


def main():
    gridsize = Grid(10,10)
    setup_game()
    


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

