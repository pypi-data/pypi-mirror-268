import pickle

def print_board(grid):
    for i in range(0, 3 * 3, 3):
        for j in range(0, 3 * 3, 3):
            print_block(i, j, grid)
        print("-" * (3 * 6 + 3))

def print_block(row_start, col_start, grid):
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            print(grid[i][j], end=" ")
        print("|", end=" ")
    print()

def has_won(board):
    # Check horizontal rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != '-':
            return True

    # Check vertical rows
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '-':
            return True

    # Check diagonal rows
    if board[0] == board[4] == board[8] != '-':
        return True
    if board[2] == board[4] == board[6] != '-':
        return True

    # No win condition found
    return False

def is_tie(board):
    if all(space != "-" for space in board):
        return True
    else:
        return False

def find_won(board):
    # Check horizontal rows
    for i in range(0, 9, 3):
        if board[i] != '-' and board[i] == board[i+1] == board[i+2]:
            return board[i]
    # Check vertical rows
    for i in range(3):
        if board[i] != '-' and board[i] == board[i+3] == board[i+6]:
            return board[i]
    # Check diagonal rows
    if board[4] != '-' and (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
        return board[4]
    if all(space != "-" for space in board):
        return "Tie"

    # No win condition found
    return "-"

def claimed_spaces(state):
    return [find_won(state[i]) for i in range(9)]


def is_game_over(state):
    claimed_spaces_var = claimed_spaces(state)
    return has_won(claimed_spaces_var) or all(item != "-" for item in claimed_spaces_var) or all(item != "-" for x in state for item in x)

def get_move(state, old_move, first_move = False):
    valid = False
    while not valid:
        move = input()
        if (len(move) == 2 
            and "0" not in move 
            and move.isdigit() 
            and state[int(move[0])-1][int(move[1])-1] == "-" 
            and (claimed_spaces(state)[int(old_move[1])-1] != "-" 
                 or int(move[0]) == int(old_move[1]) 
                 or first_move)):
            valid = True
        else:
            print("Invalid move")
    return move

def change_turn(player):
    if player == "X":
        return "O"
    else:
        return "X"
    
def generate_moves(state, old_move):
    claimed_spaces_var = claimed_spaces(state)
    valid_actions = []
    
    current_board = int(old_move[1])-1
    if claimed_spaces_var[current_board] != "-":
        for i in range(9):
            for j in range(9):
                if state[i][j] == "-":
                    valid_actions.append(f"{i+1}{j+1}")
    else:
        for j in range(9):
            if state[current_board][j] == "-":
                valid_actions.append(f"{current_board+1}{j+1}")
    if not valid_actions:
        print(f"Failed to generate moves for board {state}")
        return None
    return valid_actions

def make_move(state, move, player):
    next_state = pickle.loads(pickle.dumps(state, -1))  # Create a deep copy of the state
    next_state[int(move[0])-1][int(move[1])-1] = player
    return next_state