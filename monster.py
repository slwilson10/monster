import sys
import random
import os
import math

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
    maxGridSize = Grid(10,10)
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

    
    def draw_grid():
        # os.system('cls')
        for y in range(0,gridSize[0]+1):
                for x in range(0,gridSize[1]+1):
                    if playerPos[0] == x and playerPos[1] == y:
                        sys.stdout.write('P')
                        
                    elif monsterPos[0] == x and monsterPos[1] == y:
                        sys.stdout.write('M')
                        
                    elif treasurePos[0] == x and treasurePos[1] == y:
                        sys.stdout.write('$')
                        
                    elif trapPos[0] == x and trapPos[1] == y:
                        sys.stdout.write('T')
                        
                    elif exitPos[0] == x and exitPos[1] == y:
                        sys.stdout.write('E')

                    else:
                        sys.stdout.write('X')
                sys.stdout.write('\r\n')
    
    def player_move(playerPos):
        print('Move using WASD and E to exit.')
        choice = input('Move: ')
        if choice == 'w' and playerPos[1] != 0:
            playerPos = [playerPos[0], playerPos[1] - 1]
            return playerPos
            
        if choice == 'a' and playerPos[0] != 0:
            playerPos = [playerPos[0]- 1, playerPos[1] ]
            return playerPos
            
        if choice == 's' and playerPos[1] != gridSize[1]:
            playerPos = [playerPos[0], playerPos[1] + 1]
            return playerPos
            
        if choice == 'd' and playerPos[0] != gridSize[0]:
            playerPos = [playerPos[0] + 1, playerPos[1]]
            return playerPos
            
        if choice == 'e':
            exit_game()
   
        else:       
            print('Not a valid move')
            return playerPos
            draw_grid()
            
    def monster_move(playerPos, monsterPos):
        monX = monsterPos[0]
        monY = monsterPos[1]
        playerX = playerPos[0]
        playerY = playerPos[1]
            
        if(playerX - monX != 0):
            if(playerX - monX < 0):
                monsterPos = [monX - 1, monY]
                return monsterPos
            else:
                monsterPos = [monX + 1, monY]
                return monsterPos
        else:
            if(playerY - monY < 0):
                monsterPos = [monX, monY - 1]
                return monsterPos
            else:
                monsterPos = [monX, monY + 1]
                return monsterPos
                
    def collision_check(playerPos, monsterPos):
        
        if monsterPos == playerPos:
            print ('You were eaten by the Monster')
            exit_game()

    def exit_game():
        sys.exit()

    while True:
        draw_grid()
        monsterPos = monster_move(playerPos, monsterPos)
        collision_check(playerPos, monsterPos)

            
        playerPos = player_move(playerPos)
        print (playerPos)
        print (monsterPos)

        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

