"""Functions to be called from functions.f2 or above"""

from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes.Game import Game
from classes.SpotTakenError import SpotTakenError

from functions import ai


def game_load():
  """Returns game instance from saved.pickle, then deletes file."""
  with open("saved.pickle", "rb") as file:
    payload = pickle.load(file)
  remove("saved.pickle")
  return payload


def game_save(game):
  """Stores game instance in saved.pickle file."""
  game.loaded_now = True
  with open("saved.pickle", "wb") as file:
    pickle.dump(game, file)
  print("Game has been saved.")


def game_undo(game):
  """Removes last mark from game.board, and
  deletes corresponding coordinates from game.steps."""
  column = game.steps[game.last_player][-1][0]
  row = game.steps[game.last_player][-1][1]
  game.board[row][column] = EMPTY
  del game.steps[game.last_player][-1]
  # undo twice if AI is playing
  if ai.is_player_ai(game.last_player, game): # TODO: check last_player
    column = game.steps[game.player][-1][0]
    row = game.steps[game.player][-1][1]
    game.board[row][column] = EMPTY
    del game.steps[game.player][-1]


def handle_exit_commands(game, command):
  """Searches input string for `'u'`, `'s'`, `'q'`.
  If found, calls corresponding function and returns `True`.
  (1) `'u'` → `game_undo()`
  (2) `'s'` → `save()`
  (3) `'q'` → `quit()`
  Else, returns `None` to signal 'no exit command found'."""
  command = command.strip().lower()
  if command == 'u':
    game_undo(game)
    return True
  elif command == 's':
    game_save(game); sleep(WAIT/2)
    quit()
  elif command == 'q':
    quit()
  return None


def place_mark(coordinates, game):
  """Places player's mark at passed coordinate.
  Example input coordinates: `'a4'` → `board[3][0]`"""
  row = coordinates[1]
  column = coordinates[0]
  if row < 0:
    raise IndexError
  if game.board[row][column] == EMPTY:
    game.board[row][column] = MARKS[game.player]
    game.steps[game.player].append((column, row))
  else:
    raise SpotTakenError


def print_column_headers(board_size):
  """Prints A B C D E, etc. in a row."""
  print('  ', end='')
  for i in range(board_size):
    print(COLUMNS[i] + ' ', end='')
  print(' ')


def print_rows(game):
  """Prints each row with row number at both ends."""
  for row in range(game.board_size):
    print(str(row+1) + ' ', end='')
    for place in range(game.board_size):
      if game.winner in (0, 1) and (place, row) in game.winning_row:  # mark as winning row
        print(colored(game.board[row][place], attrs=['bold']) +
              colored('←', 'blue', attrs=['bold']), end='')
      elif (game.winner not in (0, 1)                                 # mark as last step
            and game.last_player in (0, 1)
            and game.steps[game.last_player]
            and (place, row) == game.steps[game.last_player][-1]):
        print(colored(game.board[row][place], attrs=['bold']) + 
              colored('←', 'blue', attrs=['bold']), end='')
      else:                                                           # print w/o marking
        print(colored(game.board[row][place], attrs=['bold']) + ' ', end='')
    print(str(row+1))


def quit():
  """Prints `GOODBYE` and calls `exit()` to end program."""
  print(GOODBYE); sleep(WAIT)
  system('clear')
  exit()
