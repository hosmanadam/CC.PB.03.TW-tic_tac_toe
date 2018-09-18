from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle

from data.constants import *


def did_player_win(player, game):
  """Checks board for winning_size length rows of player's mark.
  Returns coordinates for if found."""
  stop = game.winning_size-1
  shapes = {"ud":   {"range_y": (0, game.board_size - stop),
                     "range_x": (0, game.board_size),
                      "step_y": 1,
                      "step_x": 0},

            "lr":   {"range_y": (0, game.board_size),
                     "range_x": (0, game.board_size - stop),
                      "step_y": 0,
                      "step_x": 1},

            "ullr": {"range_y": (0, game.board_size - stop),
                     "range_x": (0, game.board_size - stop),
                      "step_y": 1,
                      "step_x": 1},

            "urll": {"range_y": (0, game.board_size - stop),
                     "range_x": (2, game.board_size),
                      "step_y": 1,
                      "step_x": -1}}

  for shape in shapes.values():
    for y in range(*shape["range_y"]):
      for x in range(*shape["range_x"]):
        if ([game.board[y + shape["step_y"]*i][x + shape["step_x"]*i]           # TODO - remove duplication
            for i in range(game.winning_size)] == [MARKS[player]]*game.winning_size):
          winning_row = [((x + shape["step_x"]*i), (y + shape["step_y"]*i))     # TODO - remove duplication
                         for i in range(game.winning_size)]
          return winning_row

def game_load():
  """Returns game instance from saved.pickle, then deletes file."""
  with open("saved.pickle", "rb") as file:
    payload = pickle.load(file)
  remove("saved.pickle")
  return payload

def game_save(game):
  """Stores game instance in saved.pickle file."""
  with open("saved.pickle", "wb") as file:
    pickle.dump(game, file)
  print("Game has been saved.")

def generate_board(board_size):
  """Returns 0-index list matrix populated with value of `EMPTY`.
  Matrix is square shaped (both sides are `board_size` long)
  Example: `[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]`"""
  return ([[EMPTY]*board_size for i in range(board_size)])

def get_board_size(prompt="\nWhat size board (from 3-9) "
                          "would you like to play on? "):
  """Returns value for `board_size` from user input.
  Determines actual playing area without headers, spacing, etc."""
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
  """Returns value of `players` from user inputs.
  Example: `['Adam', 'Dani']`"""
  return [input("\nEnter Player 1 name: "), input("Enter Player 2 name: ")]
  # TODO: don't allow empty input

def get_winning_size(board_size, prompt="How many marks in a row to win? "
                                        "(pick 4 or more) "):
  """Returns value of `winning_size` from user input.
  Forces correct input value."""
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

def is_it_a_tie(steps, board_size):
  """Returns `True` if board is full"""
  if len(steps[0]) + len(steps[1]) == board_size**2:
  # TODO - rewrite to analyze board instead
    return True

def place_mark(coordinates, player, game):
  """Places player's mark at passed coordinate.
  Example input coordinates: `'a4'` → `board[3][0]`"""
  row = int(coordinates[1:])-1
  if row < 0:
    raise IndexError
  column = COLUMNS.index(coordinates[0].upper())
  if game.board[row][column] == EMPTY:
    game.board[row][column] = MARKS[player]
    game.steps[player].append((column, row))
  else:
    prompt_action(player, game,
                  prompt="That spot is already taken. Try again: ")

def prompt_action(player, game, prompt=''):
  """Asks user to input coordinates. Handles 3 input cases (plus errors):
  (1) `'s'` → `save()`
  (2) `'q'` → `quit()`
  (3) coordinates → `place_mark()`"""
  try:
    action = input(prompt)
    if action.lower() == 's':
      game_save(game); sleep(WAIT/2)
      quit()
    if action.lower() == 'q':
      quit()
    place_mark(action, player, game)
  except IndexError:
    prompt_action(player, game,
                  prompt="Coordinates out of range. Try again: ")
  except ValueError:
    prompt_action(player, game,
                  prompt="Incorrectly formatted coordinates. Try again: ")

def print_board(last_player, game):
  """Prints formatted board with headers, padding and pointer arrows added in appropriate places."""
  def print_column_headers(board_size):
    """Prints A B C D E, etc. in a row."""
    print('  ', end='')
    for i in range(board_size):
      print(COLUMNS[i] + ' ', end='')
    print(' ')

  def print_rows(last_player, game):
    """Prints each row with row number at both ends."""
    for row in range(game.board_size):
      print(str(row+1) + ' ', end='')
      for place in range(game.board_size):
        if game.winner in (0, 1) and (place, row) in game.winning_row: # mark as winning row
          print(colored(game.board[row][place], attrs=['bold']) +
                colored('←', 'blue', attrs=['bold']), end='')
        elif (game.winner == None and game.steps[last_player]          # mark as last step
              and (place, row) == game.steps[last_player][-1]):
          print(colored(game.board[row][place], attrs=['bold']) + 
                colored('←', 'blue', attrs=['bold']), end='')
        else:                                                          # print w/o marking
          print(colored(game.board[row][place], attrs=['bold']) + ' ', end='')
      print(str(row+1))

  print_column_headers(game.board_size)
  print_rows(last_player, game)
  print_column_headers(game.board_size)

def print_scores(players, scores):
  """Prints current scores in one line."""
  print(f"{players[0]}: " +
        colored(f"{scores[0]}", COLORS[0]) +
        f" - {players[1]}: " +
        colored(f"{scores[1]}", COLORS[1]))

def quit():
  """Prints `GOODBYE` and calls `exit()` to end program."""
  print(GOODBYE); sleep(WAIT)
  system('clear')
  exit()

def wants_rematch(prompt=colored("\nWould you like to play another round?",
                                 attrs=['bold']) + " (y/n) "):
  """Asks user if they want to play again and returns `True` or `False` based on input."""
  intention = input(prompt)
  try:
    if intention.lower()[0] == "n":
      return False
    if intention.lower()[0] == "y":
      return True
  except IndexError:
    return wants_rematch(prompt="Type something please: ")
  return wants_rematch(prompt="Say again? ")