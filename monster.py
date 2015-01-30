import sys
import random
import os

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
        os.system('cls')
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
        print('Move using WASD')
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
   
        else:       
            print('Not a valid move')
            return playerPos
            draw_grid()
            
    def monster_move(playerPos, monsterPos):
        mon_x = monsterPos[0]
        mon_y = monsterPos[1]
        player_x = playerPos[0]
        player_y = playerPos[1]
            
        if(player_x - mon_x != 0):
            if(player_x - mon_x < 0):
                monsterPos = [mon_x - 1, mon_y]
                return monsterPos
            else:
                monsterPos = [mon_x + 1, mon_y]
                return monsterPos
        else:
            if(player_y - mon_y < 0):
                monsterPos = [mon_x, mon_y - 1]
                return monsterPos
            else:
                monsterPos = [mon_x, mon_y + 1]
                return monsterPos
    
    gameover = False
    while gameover == False:
        draw_grid()
        monsterPos = monster_move(playerPos, monsterPos)
        playerPos = player_move(playerPos)
        print (playerPos)
        print (monsterPos)
        choice = input('Escape?: ')
        if choice == 'e':
            gameover = True
        else:
            pass

        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

