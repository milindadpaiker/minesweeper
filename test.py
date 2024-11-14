
import  random
import os

GRID_SIZE = 6
SEEN = 1
UNSEEN = 0
BOMB_COUNT = 10

board = [[[UNSEEN, '?', 0] for _ in range(GRID_SIZE)] for _ in range (GRID_SIZE)]


def draw_mine_sweeper(dev_mode=False):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j][0] == UNSEEN and not dev_mode:
                print('?', end=' ')
            elif board[i][j][1] == 'B':
                #set it to blank if not a number of a bomb
                print(board[i][j][1], end=' ')                
            elif board[i][j][2] > 0:
                print(board[i][j][2], end=' ')
            else:
                print("X", end=' ')
        print()

def place_bombs():
    bombs = set()
    while len(bombs) < BOMB_COUNT:
        row = random.randint(0, GRID_SIZE-1)
        col = random.randint(0, GRID_SIZE-1)
        bombs.add((row,col))
    for b in bombs:
        board[b[0]][b[1]][1] = 'B'

def calculate_numbers():
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j][1] == 'B':
                continue
            else:
                for d in directions:
                    r = i + d[0]
                    c = j + d[1]
                    if r >= GRID_SIZE or r < 0 or c < 0 or c >= GRID_SIZE:
                        continue
                    if board[r][c][1] == 'B':
                        board[i][j][2] += 1

def check_win():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j][1] == 'B':
                continue
            elif board[i][j][0] == UNSEEN:
                return False
    return True
 
def init():
    place_bombs()
    calculate_numbers()
    

def play_game():  
    status = 'INPLAY'
    init()
    # print("----------")
    # draw_mine_sweeper(True)
    # print("----------")

    while True:
        draw_mine_sweeper()
        print("----------")
        s = input("Enter row, column: ")
        # os.system('cls')  
        r1, c1 = s.split(',') 
        r = int(r1)
        c = int(c1)

        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            board[r][c][0] = SEEN
            if board[r][c][1] == 'B':
                status= "DIED"
                break
        # check if all cells except boms seen
        if check_win() == True:
            status = "WON"
            break
    
    if status == "DIED":
        print("You died in a bomb blast")
    else:
        print("You won")

play_game()

