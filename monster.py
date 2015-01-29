import sys
import random

class Grid:
    def __init__(self, maxH, maxW):
        self.max_height = maxH
        self.max_width = maxW
        
    def grid_size(self):
        return [self.max_height, self.max_width]
            

class Character:
    def __init__(self, pos):
        self.coord = pos

    def position(self):
        return self.coord

class Player(Character):
    def __init__(self, pos):
        Character.__init__(self,pos)
        

class Monster(Character):
    def __init__(self, pos):
        Character.__init__(self, pos)

class Item:
    def __init__(self, pos):
        self.coord = pos

    def position(self):
        return self.coord

class Treasure(Item):
    def __init__(self, pos):
        Item.__init__(self, pos)

class Trap(Item):
    def __init__(self, pos):
        Item.__init__(self, pos)

class Exit(Item):
    def __init__(self, pos):
        Item.__init__(self, pos)


def main():
    maxGridSize = Grid(5,5)
    gridSize = maxGridSize.grid_size()
    coords_list = []
        
            
    def random_coords():
        check = False
        while check == False:
            position = random.randrange(0,gridSize[0] + 1 ),random.randrange(0,gridSize[1] + 1)
            if position in coords_list:
                check = False
            else:
                coords_list.append(position)
                return position
    
    player = Player(random_coords()) 
    playerPos = player.position()

    monster = Monster(random_coords())    
    monsterPos = monster.position()     

    treasure = Treasure(random_coords())    
    treasurePos = treasure.position()

    trap = Trap(random_coords())    
    trapPos = trap.position()
        
    exit = Exit(random_coords())    
    exitPos = exit.position()


    print (playerPos)
    print (monsterPos)
    print (treasurePos)
    print (trapPos)
    print (exitPos)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

