# UTTT Engine
A python library for the game of Ultimate Tic-Tac-Toe

# Documentation
Functions:
- print_board
- print_block
- has_won
- is_tie
- find_won
- claimed_spaces
- is_game_over
- get_move
- change_turn
- generate_moves
- make_move

# Definitions and important info
Game board refers to the entire game board with 9 groups and 9 spaces inside\
Group refers to one group inside a game board, can also be referred to as a board\
Old_move is set right after setting move, and is used to determine the group in which the next player can play in\
The following examples assume `from utt-engine import *`

## print_board(grid)
This function prints a given game board

Example usage:
```python
grid = [["-" for j in range(9)] for i in range(9)]

print_board(grid)
```

## print_block(row_start, col_start, grid)
This function prints one of the 9 groups. The only real use case is for the print_board function.

Example usage:
```python
grid = [["-" for j in range(9)] for i in range(9)]

for i in range(0, 3 * 3, 3):
  for j in range(0, 3 * 3, 3):
    print_block(i, j, grid)
    print("-" * (3 * 6 + 3))
```

## has_won(board)
This function returns True if either player has won (not tied) a given group, or false if not.

Example usage:  
```python
if has_won(grid[board]):
  print(f"{turn} has claimed group {board + 1}")
  for x in range(9):
    grid[board][x] = turn
```

## is_tie(board)
This function returns True if either player has tied a given group, or false if not.  

Example usage:
```python
if is_tie(claimed_spaces(grid)):
  print("Game is a tie")
```

## find_won(board)
This function returns the winner of a group. X is returned if X has won the given group, O if O has won, Tie if the group was tied, or - if none of the above are true.

Example usage:
```python
if find_won(grid[board]) == "Tie":
  print("Group has tied")
```

## claimed_spaces(board)
This function returns a list of all the groups that have been claimed given a game board.

Example usage:
```python
if has_won(claimed_spaces(grid)):
  print(f"{turn} has won")
  game = False
```

## is_game_over
This function returns True if the game is over (Tied or won), and False if not given a game board.

Example usage:
```python
if is_game_over(grid):
  print("Game is over")
```

## get_move(board, old_move)
This function gets a move from a human player via input given the game board and the previous move. If this move is invalid, "Invalid move" is printed, and nothing is returned until a valid move is played. If the move is valid, that move is returned.

Example usage:
```python
move = get_move(grid, old_move)
print(f"{move} has been played")
```

## change_turn(turn)
This function returns X if given O, and O if given X.

Example usage:
```python
turn = "X"
print(f"The current turn is {turn}")
turn = change_turn()
print(f"The current turn is now {turn}")
```

## generate_moves(board, old_move)
This function returns a list of every valid move given a game board and the previous move.

Example usage:
```python
grid = make_move(grid, random.choice(generate_moves(grid, old_move)), turn)
```

## make_move(board, move, player)
This function returns a game board after playing a move.

Example usage:
```python
print_board(grid)
make_move(grid, "11", "X")
print_board(grid)
```

# Example Game
This is an example of how to make a game of Ultimate Tic-Tac-Toe using UTT Engine. This is the code that is executed when the library is ran.

```python
while game:
    move = get_move(grid, old_move)
    old_move = move
    grid = make_move(grid, move, turn)
    claimed_spaces_var = claimed_spaces(grid)
    board = int(move[1])-1
    if has_won(grid[board]):
        print(f"{turn} has claimed group {board + 1}")
        for x in range(9):
            grid[board][x] = turn
    if has_won(claimed_spaces_var):
        print(f"{turn} has won")
        game = False
    if is_tie(claimed_spaces_var):
        print("Game is a tie")
        game = False
    print_board(grid)
    first_move = False
    turn = change_turn(turn)
```
