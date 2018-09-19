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






"""
****** STAGE 1 ******
TODO: fork main()
  ↳ do you have a friend 
  ↳ play against computer

TODO: fork action logic ("if player = 'AI'")
prompt_action() → place_mark()
ai_action()     → place_mark()

TODO: TEST random "personality"
  possibilities = find_empty_coordinates()
  place_mark(choice(possibilities))
"""



# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

def find_empty_coordinates(game):
  """Returns all coordinates on board with value `EMPTY`.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  empty_coordinates = []
  for row in range(game.board_size):
    for place in range(game.board_size):
      if board[row][place] == EMPTY:
        empty_coordinates.append((place, row))
  return empty_coordinates


def ai_action(game):
  import random
  possibilities = find_empty_coordinates(game)
  print("Computer is thinking...")
  sleep(WAIT)
  target = random.choice(possibilities)
  place_mark(target, player, game)

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑



"""
****** STAGE X ******
TODO: make it smart

"""

# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

def assign_danger_level(row):
  """Analyze rows for highest danger/potential level for both players"""
  # Reuse winning_row functionality
  # Move duplicate logic to lower level function

def find_best_row(player, game):
  """Chooses coordinates with max value from assign_danger_level()"""

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑