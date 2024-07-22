from stanfordkarel import *


def not_border(x, y, board):
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    return False


def get_min_diagonal_neighbor(x, y, board):
    
    min_value = float('inf')
    min_x = None
    min_y = None
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        new_x = x + dx
        new_y = y + dy
        if not_border(new_x, new_y, board):
            if board[new_x][new_y] < min_value:
                min_value = board[new_x][new_y]
                min_x = new_x
                min_y = new_y
    return min_x, min_y



def solve(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0  

    curr_x = 0
    curr_y = 0
    run = True

    while run:
        min_x, min_y = get_min_diagonal_neighbor(curr_x, curr_y, board)

        if min_x is None and min_y is None:
            break

        if curr_x < min_x and curr_y < min_y: #[1,1]
            board[curr_x+ 1][curr_y] += 1
            move()
            turn_left()
            move()
            three_turns()
        elif curr_x > min_x and curr_y > min_y: #[-1,-1]
            board[curr_x-1][curr_y] += 1
            two_turns()
            move()
            turn_left()
            move()
            turn_left()
        elif curr_x < min_x and curr_y > min_y: #[1,-1]
            board[curr_x+1][curr_y] += 1
            move()
            three_turns()
            move()
            turn_left()
        elif curr_x > min_x and curr_y < min_y: #[-1,1]
            board[curr_x-1][curr_y] += 1
            two_turns()
            move()
            three_turns()
            move()
            three_turns()

        curr_x = min_x
        curr_y = min_y
        board[curr_x][curr_y] += 1
        if curr_x == 0 and curr_y == 0 and any(0 in inner for inner in board): 
            for i in board:
                for j in i:
                    if j == 0: 
                        break
            run = False 




def two_turns():
   turn_left()
   turn_left()

def three_turns():
   turn_left()
   turn_left()
   turn_left()

def main():
    solve(8)


if __name__ == "__main__":
    run_karel_program()
