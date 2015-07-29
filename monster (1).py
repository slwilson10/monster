## Importing modules
import sys
import random
import os
import math

## Setting up classes and subclasses
## Probably more than actually needed
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
    def __init__(self, pos, status):
        Character.__init__(self, pos)
        self.status = status
        
    def awake(self):
        return self.status

class Item:
    def __init__(self, pos):
        self.coord = pos

    def position(self):
        return self.coord

class Treasure(Item):
    def __init__(self, pos, status):
        Character.__init__(self, pos)
        self.status = status
        
    def collected(self):
        return self.status

class Trap(Item):
    def __init__(self, pos):
        Item.__init__(self, pos)
        
class Exit(Item):
    def __init__(self, pos):
        Item.__init__(self, pos)


## Starting main function
def main():
        
    ## Returns tuple of random numbers as coords      
    def random_coords():
        check = False
        while check == False:
            position = random.randrange(0,gridSize[0] + 1 ),random.randrange(0,gridSize[1] + 1)
            if position in coords_list:
                check = False
            else:
                coords_list.append(position)
                return position
    
    ## Draws the game board
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
                    
                    elif exitPos[0] == x and exitPos[1] == y:
                        sys.stdout.write('E')
                    
                    elif (x, y) in showTraps:
                        
                        sys.stdout.write('T')

                    else:
                        sys.stdout.write('X')
                sys.stdout.write('\r\n')
    
    ## User chooses size of game board
    def choose_gridsize():
            os.system('cls')
            print('Level size? 5-10')
            while True:
                try:
                    sizeChoice = int(input('Choice?: '))

                except ValueError:
                    print ("Please enter a number.")
                    continue
            
                if sizeChoice < 5 or sizeChoice > 10:
                    print ('Not a valid choice')
                
                else:
                    return sizeChoice
            
    ## User chooses game difficulty
    def choose_difficulty(newSize):
            print('Difficulty? 1(Easy), 2(Medium), 3(Hard)')
            while True:
                try:
                    diffChoice = int(input('Choice?: '))
                
                except ValueError:
                    print ("Please enter a number.")
                    continue
                    
                if diffChoice > 1 or diffChoice < 3:
                    if diffChoice == 1:
                        return math.trunc(newSize/2) - 1
                        
                    elif diffChoice == 2:
                        return math.trunc(newSize/2) + 1
                        
                    elif diffChoice == 3:
                        return math.trunc(newSize/2) + 2
                        
                    else:
                        print ('Something went wrong')
                        break

                else:
                    print ('Not a valid choice')
                    continue

    ## Moves player across board
    def player_move(playerPos):
        print('Move using WASD and E to exit.')
        choice = input('Move: ')
        if choice == 'w' and playerPos[1] != 0:
            playerPos = (playerPos[0], playerPos[1] - 1)
            return playerPos
            
        if choice == 'a' and playerPos[0] != 0:
            playerPos = (playerPos[0]- 1, playerPos[1] )
            return playerPos
            
        if choice == 's' and playerPos[1] != gridSize[1]:
            playerPos = (playerPos[0], playerPos[1] + 1)
            return playerPos
            
        if choice == 'd' and playerPos[0] != gridSize[0]:
            playerPos = (playerPos[0] + 1, playerPos[1])
            return playerPos
            
        if choice == 'e':
            exit_game()
   
        else:       
            print('Not a valid move')
            return playerPos
            draw_grid()
            
    ## Moves monster towards player
    def monster_move(playerPos, monsterPos):
        monX = monsterPos[0]
        monY = monsterPos[1]
        playerX = playerPos[0]
        playerY = playerPos[1]
           
        if(playerX - monX != 0):
            if(playerX - monX < 0):
                monsterPos = (monX - 1, monY)
                return monsterPos
            else:
                monsterPos = (monX + 1, monY)
                return monsterPos
        else:
            if(playerY - monY < 0):
                monsterPos = (monX, monY - 1)
                return monsterPos
            else:
                monsterPos = (monX, monY + 1)
                return monsterPos
                
    ## Checks if monster is next to player
    def monster_check(playerPos, monsterPos):
        if playerPos == monsterPos:
            print ('You were eaten by the Monster!')
            input("Press Enter to continue...")
            exit_game()
        else:
            pass
            
    ## Checks if player trips a trap
    def trap_check(playerPos, traps):
        if playerPos in traps:
            print ('You awoke the Monster!')
            input("Press Enter to continue...")
            return True 
        else:
            return False
    
    ## Checks if player collides with treasure
    def treasure_check(playerPos, treasurePos):
        if playerPos == treasurePos:
            print ('You collected the treasure!')
            input("Press Enter to continue...")
            return True 
        else:
            return False
    
    ## Checks if player collides with exit      
    def exit_check(playerPos, exitPos):
        if playerPos == exitPos:
            print ('You escaped safely!')
            input("Press Enter to continue...")
            return True 
        else:
            return False

    ## Exits program
    def exit_game():
        sys.exit()   
    
    ## Shows start screen and options
    def start_screen():
        while True:
            os.system('cls')
            print ('++++++++++++++++++++++')
            print ('++++++++++++++++++++++')
            print ('++      MONSTER     ++')
            print ('++++++++++++++++++++++')
            print ('++++++++++++++++++++++')
            print('1 (Start New Game)')
            print('2 (How to Play)')
            print('3 (Exit)')
        
            try:
                choice = int(input('Choice?: '))
                
            except ValueError:
                    print ("Please enter a number.")
                    continue
                    
            if choice == 1:
                    break
                        
            elif choice == 2:
                        print ('Move the player (P) through the dungeon to reach the treasure ($).')
                        print ('Once the treasure is collected, race to the exit (E) of the dungeon.')
                        print ('Careful not to step on the hidden traps (T) that awaken the monster (M).')
                        input("Press Enter to continue...")
                        continue
                        
            elif choice == 3:
                    exit_game()
                        
            else:
                print ('Not a valid choice')
                continue
                
    ## Starting of the program          
    start_screen()
    ## Choose size of the game board
    newSize = choose_gridsize()
    maxGridSize = Grid(newSize,newSize)     
    gridSize = maxGridSize.grid_size()
    ## Choose difficulty
    numberOfTraps = choose_difficulty(newSize)
    ## Holds position of all items to avoid overlap
    coords_list = []
    ## Init Player at random position
    player = Player(random_coords()) 
    playerPos = player.position()
    ## Init Monster at random position
    monster = Monster(random_coords(), False)    
    monsterPos = monster.position()  
    ## Init Treasure at random position
    treasure = Treasure(random_coords(), False)   
    treasurePos = treasure.position()
    ## Empty list the will hold tripped traps
    showTraps = []
    ## Holds postion for all the traps
    traps = []
    ## Gives id number to each trap, probably not needed
    trapNumber = 0
    while  len(traps) < numberOfTraps:
            
            newTrap = Trap(random_coords())
            traps.append(newTrap.position())
    ## Init Exit at random position      
    exit = Exit(random_coords())    
    exitPos = exit.position()
    
    ## Game loop
    while True:
        draw_grid()
        
        if monster.awake():
            monster_check(playerPos, monsterPos)
            monsterPos = monster_move(playerPos, monsterPos)
            monster_check(playerPos, monsterPos)
        else:
            if trap_check(playerPos, traps):
                ## If player collides with trap, show where the hidden traps are
                for t in traps:
                    showTraps.append(t)
                ## Start the monster chasing the player
                monster =  Monster(monsterPos, True) 

            else:
                pass
        
        if treasure.collected():
            if exit_check(playerPos, exitPos):
                print ('You won the game!')
                exit_game()
                
            else:
                pass
        else: 
            if treasure_check(playerPos, treasurePos):
                treasure = Treasure(treasurePos, True)

            
        playerPos = player_move(playerPos)
        

        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

