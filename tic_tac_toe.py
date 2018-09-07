from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
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
          # TODO = Set winning_row coordinates
          return True

def game_load():
  with open("saved.pickle", "rb") as file:
    payload = pickle.load(file)
  remove("saved.pickle")
  return payload

def game_new():
  board_size = get_board_size()
  payload = board_size, get_to_win(board_size), get_player_names(), [0, 0], 0
  return payload

def game_save():
  with open("saved.pickle", "wb") as file:
    pickle.dump((board_size, to_win, players, scores, board, steps,
                 current_player), file)
  print("Game has been saved.")

def generate_board():
  return ([[EMPTY]*board_size for i in range(board_size)])

def get_board_size(prompt="\nWhat size board (from 3-9) "
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

def get_to_win(board_size, prompt="How many marks in a row to win? "
                                  "(pick 4 or more) "):
  if board_size == 3:
    print("Place 3 marks in a row to win!")
    return 3
  if board_size == 4:
    print("Place 4 marks in a row to win!")
    return 4
  if board_size > 4:
    minimum, maximum = 4, board_size
  try:
    to_win = int(input(prompt))
  except ValueError:
    return get_to_win(board_size,
                      prompt=f"You have to enter a natural number between "
                             f"{minimum} and {maximum}. Try again: ")
  if to_win > maximum:
    return get_to_win(board_size, 
                      prompt="Winning size can't be larger than board. "
                             "Try again: ")
  if to_win < minimum:
    return get_to_win(board_size, 
                      prompt=f"Winning size has to be between {minimum} and "
                             f"{maximum}. Try again: ")
  return to_win

def is_it_a_tie():
  if len(steps[0]) + len(steps[1]) == board_size**2 and winner == None:
    return True

def place_mark(player, coordinates):
    row = int(coordinates[1:])-1
    if row < 0:
      raise IndexError
    column = COLUMNS.index(coordinates[0].upper())
    if board[row][column] == EMPTY:
      board[row][column] = MARKS[player]
      steps[player].append((column, row))
    else:
      prompt_action(player, prompt="That spot is already taken. Try again: ")

def prompt_action(player, prompt=''):
  try:
    action = input(prompt)
    if action.lower() == 's':
      game_save(); sleep(WAIT/2)
      quit()
    if action.lower() == 'q':
      quit()
    place_mark(player, action)
  except IndexError: 
    prompt_action(player, prompt="Coordinates out of range. Try again: ")
  except ValueError: 
    prompt_action(player, prompt="Incorrectly formatted coordinates. "
                                 "Try again: ")

def print_board(last_player):
  """v1: Minimalistic version without grid, with bold marks"""
  def print_column_headers():
    print('  ', end='')
    for i in range(board_size):
      print(COLUMNS[i] + ' ', end='')
    print(' ')

  def print_rows(last_player):
    for row in range(board_size):
      print(str(row+1) + ' ', end='')
      for place in range(len(board[row])):
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
        # if winner in (0, 1) and ...:
        #   print("Somebody's won!")
# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
        if (winner == None and steps[last_player] # ELIF AFTER WINNER
            and (place, row) == steps[last_player][-1]):
          print(colored(board[row][place], attrs=['bold']) + 
                colored('←', 'blue', attrs=['bold']), end='')
        else:
          print(colored(board[row][place], attrs=['bold']) + ' ', end='')
      print(str(row+1))

  print_column_headers()
  print_rows(last_player)
  print_column_headers()

def print_scores():
  print(f"{players[0]}: " +
        colored(f"{scores[0]}", COLORS[0]) +
        f" - {players[1]}: " +
        colored(f"{scores[1]}", COLORS[1]))

def quit():
  print(GOODBYE); sleep(WAIT)
  system('clear')
  exit()

def wants_rematch(prompt=colored("\nWould you like to play another round?",
                                 attrs=['bold']) + " (y/n) "):
  intention = input(prompt)
  try:
    if intention.lower()[0] == "n":
      return False
    if intention.lower()[0] == "y":
      return True
  except IndexError:
    return wants_rematch(prompt="Type something please: ")
  return wants_rematch(prompt="Say again? ")


# Create constants
COLUMNS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Included whole ABC for error handling
COLORS = ['red', 'green']
MARKS = [colored('X', COLORS[0]), colored('O', COLORS[1])]
EMPTY = ' '
WAIT = 1.5
WELCOME = ("*** Hello and welcome to " + colored("Tic-tac-toe ", attrs=['bold'])
         + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***")
WELCOME_BACK = ["*** Welcome back to " + colored("Tic-tac-toe ", attrs=['bold'])
              + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***",
                "Continuing from where you left off..."]
GOODBYE = ("\n*** Thanks for playing. " + colored("Goodbye!", attrs=['bold']) +
           " ***")
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
  system('clear')
  try:
    board_size, to_win, players, scores, board, steps, current_player = game_load()
    print(WELCOME_BACK[0]); sleep(WAIT)
    print(WELCOME_BACK[1]); sleep(WAIT)
    system('clear')
    from_load = True           # HACK 1
  except FileNotFoundError:
    print(WELCOME); sleep(WAIT)
    board_size, to_win, players, scores, current_player = game_new()
    print("\nLet's begin..."); sleep(WAIT)
    from_load = False          # HACK 1
  wants_to_play = True
  while wants_to_play:
    if not from_load:          # HACK 1
      board = generate_board() # HACK 1
      steps = [[], []]         # HACK 1
    winner = None
    while winner == None:
      for player in range(2):  
        if not from_load:      # HACK 1
          system('clear')      # HACK 1
        from_load = False      # HACK 1
        if player == 0 and len(steps[0]) > len(steps[1]):
          continue # Makes loaded game start with next player
        print_scores(); print('')
        print(INSTRUCTIONS)
        last_player = [x for x in (0, 1) if x != player][0]
        print_board(last_player)
        print(colored(f"\n{players[player]}", COLORS[player], attrs=['bold']) +
                       ", make your move: ", end='')
        prompt_action(player)
        if is_it_a_tie():
          winner = 'tie'                                                # HACK 2                                                        # HACK 2
          system('clear')                                               # HACK 2
          print('\n'*5)                                                 # HACK 2
          print_board(last_player)                                      # HACK 2
          print(colored("\nIt's a tie!", attrs=['bold'])); sleep(WAIT)  # HACK 2
          print_scores(); sleep(WAIT)                                   # HACK 2
          wants_to_play = wants_rematch()                               # HACK 2
          break                                                         # HACK 2
        if did_player_win(player):
          winner = player
          system('clear')
          print('\n'*5)
          print_board(last_player) # TODO - PASS WINNER
          print(colored(f"\n{players[player]} wins in {len(steps[player])} "
                         "steps!", COLORS[player], attrs=['bold'])); sleep(WAIT)
          scores[player] += 1
          print_scores(); sleep(WAIT)
          wants_to_play = wants_rematch()
          break
  quit()
except KeyboardInterrupt:
  print('')
  quit()