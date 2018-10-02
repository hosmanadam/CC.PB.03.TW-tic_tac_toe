"""AI module for Tic-tac-toe"""

from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes import Game, SpotTakenError

from functions import f3


def ai_action(player, game):
  """Prints AI 'thinking process' and places mark in random empty spot."""
  possibilities = find_empty_coordinates(game)
  target = random.choice(possibilities)
  sleep(WAIT/2)
  for i in range(3):
    print('.', end='', flush=True); sleep(WAIT/2)
  print(f" {COLUMNS[target[0]].lower()}", end='', flush=True); sleep(WAIT/10)
  print(target[1]+1, end='', flush=True); sleep(WAIT/3)
  f3.place_mark(target, player, game)


def find_empty_coordinates(game):
  """Returns all coordinates on board with value `EMPTY`.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  empty_coordinates = []
  for row in range(game.board_size):
    for column in range(game.board_size):
      if game.board[row][column] == EMPTY:
        empty_coordinates.append((column, row))
  return empty_coordinates


# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ MAKING IT SMART ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓


"""
BEFORE:
  f2.ai_action() gets empty spots from find_empty_coordinates() and places mark in random one.


AFTER:
  After each place_mark(), main() uses find_best_rows() to:

    1.) analyze board 

    2.) store most dangerous rows of both players in game.best_rows
        (with extension coordinates* and danger level**)
        Example: `[
                   {'danger': 2,
                    'rows': [
                             {'row': [(0, 1), (0, 2), (0, 3)], 'extension': [(0, 0), (0, 4)]},
                             {'row': [(1, 1), (1, 2), (1, 3)], 'extension': [(1, 0), (1, 4)]}
                            ]
                   },

                   {'danger': 1,
                    'rows': [
                             {'row': [(3, 0), (3, 1), (3, 2), (3, 3)], 'extension': [(3, 4)]},
                             {'row': [(5, 1), (5, 2), (5, 3), (5, 4)], 'extension': [(5, 0), (5, 5)]}
                            ]
                   }
        *  extension coordinates:  denote open positions immediately next to row on either side
        ** danger level:  integer value representing N steps away from winning row
                          Examples:
                            0: winning row
                            1: one extension needed to become winning row


  This information is later used in 2 places.

    1.) find_winning_row() searches game.best_rows for danger level 0
        if found:
          handle_match_end()

    2.) ai_action() looks at danger levels in game.best_rows
        if AI's best row same/better level as opponent's:
          place_mark(to extend opponent's row) # strategy: offensive
        else:
          place_mark(to extend AI's row)       # strategy: defensive

INBOX
  if same extension coordinate accompanies multiple rows:
    choose that (2 birds, 1 stone)
  else:
    choose random

  if no steps yet: place in middle

"""


def assign_danger_level(row):
  """Analyze rows for highest danger/potential level for both players"""
  # Reuse winning_row functionality
  # Move duplicate logic to lower level function

def find_best_rows(player, game):
  """returns coordinates of rows with highest danger level for both players.
  example: [[player0bestrows][player1bestrows]]"""


# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑
