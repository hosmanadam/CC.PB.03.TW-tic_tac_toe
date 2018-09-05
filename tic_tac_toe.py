from sys import exit
from termcolor import colored


def did_player_win(player):
  stop = to_win-1
  shapes = {"ud":   {"range_y": (0, board_size - stop),
                     "range_x": (0, board_size),
                     "step_y": 1,
                     "step_x": 0},

            "lr":   {"range_y": (0, board_size),
                     "range_x": (0, board_size - stop),
                     "step_y": 0,
                     "step_x": 1},

            "ullr": {"range_y": (0, board_size - stop),
                     "range_x": (0, board_size - stop),
                     "step_y": 1,
                     "step_x": 1},

            "urll": {"range_y": (2, board_size - stop),
                     "range_x": (0, board_size - stop),
                     "step_y": -1,
                     "step_x": 1}}
  
  for shape in shapes.values():
    for y in range(*shape["range_y"]):
      for x in range(*shape["range_x"]):
        if [board[y + shape["step_y"]*i][x + shape["step_x"]*i] for i in range(to_win)] == [MARKS[player]]*to_win:
          return True

def generate_board():
  return ([[EMPTY]*board_size for i in range(board_size)])

def get_board_size(prompt="What size board (from 3-9) would you like to play on? "):
  """Determines actual playing area without headers, spacing, etc."""
  return int(input(prompt))

def get_player_names():
  return [input("Enter Player 1 name: "), input("Enter Player 2 name: ")]

def get_to_win():
  return int(input("How many marks in a row to win? "))

def placement(player):
  coordinates = input(f"{players[player]}, enter your coordinates (e.g. a1, c2): ")
  # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
  if coordinates[0].lower() == 's':
    save()
    exit()
  if coordinates[0].lower() == 'q':
    exit()
  # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
  row = int(coordinates[1:])-1
  column = COLUMNS.index(coordinates[0].upper())
  if board[row][column] == EMPTY:
    board[row][column] = MARKS[player]
  else:
    print("That's spot is already taken.")
    placement(player)

# def print_board():
#   """v0: For testing purposes"""
#   print(100*'\n')
#   for row in board:
#     print(row)

def print_board():
  """v1: Minimalistic version without grid, with bold marks"""
  def print_column_headers():
    print('  ', end='')
    for i in range(board_size):
      print(COLUMNS[i] + ' ', end='')
    print(' ')

  def print_column_footers():
    print('  ', end='')
    for i in range(board_size):
      print('↑ ', end='')
    print(' ')

  def print_rows():
    for i in range(board_size):
      print(str(i+1) + ' ', end='')
      for place in board[i]:
        print(colored(place, attrs=['bold']) + ' ', end='')
      print(str(i+1)) # A
      # print('←') # B

  print(100*'\n')
  print_column_headers()
  print_rows()
  print_column_headers() # A
  # print_column_footers() # B


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
import pickle
def save():
    save = players, board, scores, board_size, to_win
    with open("save.pickle", "wb") as file:
      pickle.dump(save, file)
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑


print(100*'\n')

COLUMNS = 'ABCDEFGHI'
MARKS = 'XO'
EMPTY = ' '
board_size = get_board_size()
to_win = get_to_win()
players = get_player_names()

board = []
scores = [0, 0]
wants_to_play = True


while wants_to_play:
  board = generate_board()
  print_board()
  winner = None
  while not winner:
    for player in range(2):      
      placement(player)
      print_board()
      if did_player_win(player):
        print(f"{players[player]} wins!")
        winner = players[player]
        scores[player] += 1
        print(scores)
        if input("Would you like to play again? (y/n) ").lower()[0] == "n":
          wants_to_play = False
        break