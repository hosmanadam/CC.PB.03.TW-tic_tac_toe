from sys import exit
from os import remove
from termcolor import colored
import pickle


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
        if ([board[y + shape["step_y"]*i][x + shape["step_x"]*i]
            for i in range(to_win)] == [MARKS[player]]*to_win):
          return True

def generate_board():
  return ([[EMPTY]*board_size for i in range(board_size)])

def get_board_size(prompt="What size board (from 3-9) "
                          "would you like to play on? "):
  """Determines actual playing area without headers, spacing, etc."""
  try:
    board_size = int(input(prompt))
  except ValueError:
    return get_board_size(prompt="You have to enter a natural number between "
                                 "3 and 9. Try again: ")
  if board_size not in range(3, 10):
    return get_board_size(prompt="Board size has to be between 3 and 9. "
                                 "Try again: ")
  return board_size

def get_player_names():
  return [input("\nEnter Player 1 name: "), input("Enter Player 2 name: ")]

def get_to_win(prompt="How many marks in a row (from 3-5) to win? "):
  try:
    to_win = int(input(prompt))
  except ValueError:
    return get_to_win(prompt="You have to enter a natural number between "
                             "3 and 5. Try again: ")
  if to_win not in range(3, 6):
    return get_to_win(prompt="Winning size has to be between 3 and 5. "
                             "Try again: ")
  return to_win

def place_mark(player, coordinates):
    row = int(coordinates[1:])-1
    if row < 0:
      raise IndexError
    column = COLUMNS.index(coordinates[0].upper())
    if board[row][column] == EMPTY:
      board[row][column] = MARKS[player]
    else:
      prompt_action(player, prompt="That spot is already taken. Try again: ")

def prompt_action(player, prompt=''):
  try:
    action = input(prompt)
    if action.lower() == 's':
      game_save()
      quit()
    if action.lower() == 'q':
      quit()
    place_mark(player, action)
  except IndexError: 
    prompt_action(player, prompt="No such place on this board. Try again: ")
  except ValueError: 
    prompt_action(player, prompt="Incorrectly formatted coordinates. "
                                 "Try again: ")

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

  def print_rows():
    for i in range(board_size):
      print(str(i+1) + ' ', end='')
      for place in board[i]:
        print(colored(place, attrs=['bold']) + ' ', end='')
      print(str(i+1))

  print_column_headers()
  print_rows()
  print_column_headers()

def print_scores():
  print(f"{players[0]}: " +
        colored(f"{scores[0]}", COLORS[0]) +
        f" - {players[1]}: " +
        colored(f"{scores[1]}\n", COLORS[1]))

# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
def game_save():
  with open("saved.pickle", "wb") as file:
    pickle.dump((board_size, to_win, players, scores, board, steps), file)
  print("\nGame has been saved.", end='')

def game_load():
  with open("saved.pickle", "rb") as file:
    payload = pickle.load(file)
  remove("saved.pickle")
  return payload

def game_new():
  return get_board_size(), get_to_win(), get_player_names(), [0, 0]
  scores = [0, 0]
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑

def quit():
  print(GOODBYE)
  exit()


# Create constants
COLUMNS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Included whole ABC for error handling
COLORS = ['red', 'green']
MARKS = [colored('X', COLORS[0]), colored('O', COLORS[1])]
EMPTY = ' '
HELLO = ("*** Hello and welcome to " + colored("Tic-tac-toe ", attrs=['bold'])
         + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***\n")
GOODBYE = ("\n*** Thanks for playing. " + colored("Goodbye!", attrs=['bold']) +
           " ***\n")
INSTRUCTIONS = ("Save game and exit: 's'\n"
                "Exit without saving: 'q'\n" +
                colored("Place mark by entering its coordinates "
                        "(e.g. 'a1', 'c2'):\n", attrs=['bold']))
# Create game variables
board_size = None
to_win = None
players = []
scores = []
# Create round variables
board = []
steps = []


try:
  print('\n'*100 + HELLO)
  try:
    board_size, to_win, players, scores, board, steps = game_load()
    from_load = True # HACK
  except FileNotFoundError:
    board_size, to_win, players, scores = game_new()
    from_load = False # HACK
  wants_to_play = True
  while wants_to_play:
    if not from_load:
      board = generate_board()
      steps = [0, 0]
    from_load = False # HACK
    winner = None
    while not winner:
      for player in range(2):  
        print('\n'*100)
        if sum(scores) > 0:
          print_scores()
        print(INSTRUCTIONS)
        print_board()
        print(colored(f"\n{players[player]}", COLORS[player], attrs=['bold']) +
                       ", make your move: ", end='')
        prompt_action(player)
        steps[player] += 1
        if did_player_win(player):
          print("\n"*100)
          print_board()
          print(colored(f"\n{players[player]} wins in {steps[player]} steps!",
                        COLORS[player], attrs=['bold']))
          winner = players[player]
          scores[player] += 1
          if sum(scores) > 1:
            print_scores()
          if input(colored("Would you like to play again?", attrs=['bold']) + 
                   " (y/n) ").lower()[0] == "n":
            wants_to_play = False
          break
  quit()
except KeyboardInterrupt:
  print('')
  quit()