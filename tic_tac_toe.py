from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle


def did_player_win(player):
  stop = winning_size-1
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

            "urll": {"range_y": (0, board_size - stop),
                     "range_x": (2, board_size),
                      "step_y": 1,
                      "step_x": -1}}

  for shape in shapes.values():
    for y in range(*shape["range_y"]):
      for x in range(*shape["range_x"]):
        if ([board[y + shape["step_y"]*i][x + shape["step_x"]*i]            # TODO - remove duplication
            for i in range(winning_size)] == [MARKS[player]]*winning_size):
          winning_row = [((x + shape["step_x"]*i), (y + shape["step_y"]*i)) # TODO - remove duplication
                         for i in range(winning_size)]
          return True

def game_load():
  with open("saved.pickle", "rb") as file:
    payload = pickle.load(file)
  remove("saved.pickle")
  return payload

def game_new():
  board_size = get_board_size()
  payload = board_size, get_winning_size(board_size), get_player_names(), [0, 0], 0
  return payload

def game_save():
  with open("saved.pickle", "wb") as file:
    pickle.dump((board_size, winning_size, players, scores, board, steps,
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

def get_winning_size(board_size, prompt="How many marks in a row to win? "
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
    winning_size = int(input(prompt))
  except ValueError:
    return get_winning_size(board_size,
                            prompt=f"You have to enter a natural number between "
                                   f"{minimum} and {maximum}. Try again: ")
  if winning_size > maximum:
    return get_winning_size(board_size, 
                            prompt="Winning size can't be larger than board. "
                                   "Try again: ")
  if winning_size < minimum:
    return get_winning_size(board_size, 
                            prompt=f"Winning size has to be between {minimum} and "
                                   f"{maximum}. Try again: ")
  return winning_size

def is_it_a_tie():
  if len(steps[0]) + len(steps[1]) == board_size**2:
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

def print_board(last_player, winner):
  """v1: Minimalistic version without grid, with bold marks"""
  def print_column_headers():
    print('  ', end='')
    for i in range(board_size):
      print(COLUMNS[i] + ' ', end='')
    print(' ')

  def print_rows(last_player, winner):
    for row in range(board_size):
      print(str(row+1) + ' ', end='')
      for place in range(board_size):
        if winner in (0, 1) and (place, row) in winning_row: # mark as winning row
          print(colored(board[row][place], attrs=['bold']) +
                colored('←', 'blue', attrs=['bold']), end='')
        elif (winner == None and steps[last_player]          # mark as last step
            and (place, row) == steps[last_player][-1]):
          print(colored(board[row][place], attrs=['bold']) + 
                colored('←', 'blue', attrs=['bold']), end='')
        else:                                                # print w/o marking
          print(colored(board[row][place], attrs=['bold']) + ' ', end='')
      print(str(row+1))

  print_column_headers()
  print_rows(last_player, winner)
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


if __name__ == '__main__':
  def main():
    import data.variables as v
    import data.constants as c
    try:
      system('clear')
      try:
        v.board_size, v.winning_size, v.players, v.scores, v.board, v.steps, current_player = game_load()
        print(c.WELCOME_BACK[0]); sleep(c.WAIT)
        print(c.WELCOME_BACK[1]); sleep(c.WAIT)
        from_load = True             # HACK 1
      except FileNotFoundError:
        print(c.WELCOME); sleep(c.WAIT)
        v.board_size, v.winning_size, v.players, v.scores, current_player = game_new()
        print("\nLet's begin..."); sleep(c.WAIT)
        from_load = False            # HACK 1
      wants_to_play = True
      while wants_to_play:
        if not from_load:            # HACK 1 - resets round variables if game is new, not loaded
          v.board = generate_board() # HACK 1
          v.steps = [[], []]         # HACK 1
        from_load = False            # HACK 1
        winner = None
        while winner == None:
          for player in range(2):
            system('clear')
            if player == 0 and len(v.steps[0]) > len(v.steps[1]):
              continue # Makes loaded game start with next player
            print_scores(); print('')
            print(c.INSTRUCTIONS)
            last_player = [x for x in (0, 1) if x != player][0]
            print_board(last_player, winner)
            print(colored(f"\n{v.players[player]}", c.COLORS[player], attrs=['bold']) +
                           ", make your move: ", end='')
            prompt_action(player)
            if did_player_win(player):
              winner = player
              system('clear')
              print('\n'*5)
              print_board(last_player, winner)
              print(colored(f"\n{v.players[player]} wins in {len(v.steps[player])} "
                             "steps!", c.COLORS[player], attrs=['bold'])); sleep(c.WAIT)
              v.scores[player] += 1
              print_scores(); sleep(c.WAIT)
              wants_to_play = wants_rematch()
              break
            if is_it_a_tie():
              winner = 'tie'                                                  # HACK 2 - duplicate of winning scenario
              system('clear')                                                 # HACK 2   w/ minor modifications
              print('\n'*5)                                                   # HACK 2
              print_board(last_player, winner)                                # HACK 2
              print(colored("\nIt's a tie!", attrs=['bold'])); sleep(c.WAIT)  # HACK 2
              print_scores(); sleep(c.WAIT)                                   # HACK 2
              wants_to_play = wants_rematch()                                 # HACK 2
              break                                                           # HACK 2
      quit()
    except KeyboardInterrupt:
      print('')
      quit()

  main()