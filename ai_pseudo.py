"""

input "Player vs. Computer or Player vs. Player"
if player vs. computer:
computerMoves:
    if computerStartsTheGame:

    first step = center

    if computerCanWin:
        moveThere
    elif playerCanWin:
        moveThere

    elif computerCanWin -1
        moveNearby
    elif playerCanWin -1
        moveNearby

    elif computerCanWin -2 
        moveNearby
    elif playerCanWin -2
        moveNearby

    if playerStartsTheGame:

    if playerCanWin:
    moveThere

    elif computerCanWin:
    moveThere

    elif playerCanWin -1
        moveNearby

    elif computerCanWin -1
        moveNearby

    elif playerCanWin -2
        moveNearby

    elif computerCanWin -2
        moveNearby


computerCanWin = if it need 1 more mark to reach "isWinner"
moveThere = winning row index + 1

"""



# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

def find_empty_coordinates(game):
  """Returns all coordinates on board with value `EMPTY`.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  empty_coordinates = []
  for row in game.board:
      for mark in row:
        if mark == EMPTY:
            empty_coordinates.append(mark)
          return 

def find_empty_coordinates(game):
  """Returns all coordinates on board with value `EMPTY`.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  empty_coordinates = []
  for row in range(game.board_size):
      for place in range(game.board_size):
        if board[row][place] == EMPTY:
            empty_coordinates.append((place, row))
  return empty_coordinates


def ai_action():
  import random
  possibilities = find_empty_coordinates()
  print("Computer is thinking...")
  sleep(WAIT)
  place_mark(possibilities.random)

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑



"""

STAGE 1:
TODO: fork main()
  ↳ do you have a friend 
  ↳ play against computer

TODO: fork action logic ("if player = 'AI'")
prompt_action() → place_mark()
ai_action() →     place_mark()

TODO: random "personality"
  possibilities = find_empty_coordinates()
  place_mark(choice(possibilities))


STAGE X
TODO: refactor find_winning_row

  # reuse winning_row functionality
  find_winning_row(player, game)            
  find_best_row(player, game)               # analyzes rows for potential

  # move duplicate logic to lower level function
  find_longest_row(player, game, iteration)
  
"""
