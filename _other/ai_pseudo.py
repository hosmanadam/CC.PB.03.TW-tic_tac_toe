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


"""STRATEGY NOTES

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