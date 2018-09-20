"""Functions to be called from functions.f2 or above"""

from os import remove, system
from sys import exit, stdout
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes import Game, SpotTakenError


# AI stuff
def find_empty_coordinates(game):
  """Returns all coordinates on board with value `EMPTY`.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  empty_coordinates = []
  for row in range(game.board_size):
    for column in range(game.board_size):
      if game.board[row][column] == EMPTY:
        empty_coordinates.append((column, row))
  return empty_coordinates


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


def place_mark(coordinates, player, game):
  """Places player's mark at passed coordinate.
  Example input coordinates: `'a4'` → `board[3][0]`"""
  row = coordinates[1]
  column = coordinates[0]
  if row < 0:
    raise IndexError
  if game.board[row][column] == EMPTY:
    game.board[row][column] = MARKS[player]
    game.steps[player].append((column, row))
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
      if game.winner in (0, 1) and (place, row) in game.winning_row: # mark as winning row
        print(colored(game.board[row][place], attrs=['bold']) +
              colored('←', 'blue', attrs=['bold']), end='')
      elif (game.winner == None and game.steps[game.last_player]          # mark as last step
            and (place, row) == game.steps[game.last_player][-1]):
        print(colored(game.board[row][place], attrs=['bold']) + 
              colored('←', 'blue', attrs=['bold']), end='')
      else:                                                          # print w/o marking
        print(colored(game.board[row][place], attrs=['bold']) + ' ', end='')
    print(str(row+1))


def quit():
  """Prints `GOODBYE` and calls `exit()` to end program."""
  print(GOODBYE); sleep(WAIT)
  system('clear')
  exit()
