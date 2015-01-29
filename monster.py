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
        

class Monster(Character):
    pass

class Item:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        
    def position(self):
        return [self.positionX, self.positionY]

class Treasure(Item):
    pass

class Trap(Item):
    pass

class Exit(Item):
    pass

def random_place(gridSize):
    position = [random.randint(0,gridSize[0] - 1),random.randint(0,gridSize[1] - 1)]    
    return position
        
def check_overlap(pos1, pos2):
    
    if pos1 == pos2:
        return False
    
    
    return playerPos[7,7]
        
        
    
    


def main():
    maxGridSize = Grid(5,5)
    gridSize = maxGridSize.grid_size()
    
    player = Character(random_place(gridSize)[0],random_place(gridSize)[1])
    playerPos = player.position()
    monster = Character(random_place(gridSize)[0],random_place(gridSize)[1])
    monsterPos = monster.position()
    treasure = Item(random_place(gridSize)[0],random_place(gridSize)[1])
    treasurePos = treasure.position()
    trap = Item(random_place(gridSize)[0],random_place(gridSize)[1])
    trapPos = trap.position()
    exit = Item(random_place(gridSize)[0],random_place(gridSize)[1])
    exitPos = exit.position()
    
    print (playerPos)
    print (monsterPos)
    print (treasurePos)
    print (trapPos)
    print (exitPos)
    
    check_overlap(playerPos, monsterPos, treasurePos, trapPos, exitPos, gridSize)
    
    print (playerPos)
    print (monsterPos)
    print (treasurePos)
    print (trapPos)
    print (exitPos)

    


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

