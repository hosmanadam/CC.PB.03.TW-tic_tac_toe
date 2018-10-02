"""Main module for Tic-tac-toe"""

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


def assign_danger_level(row):
  """Analyze rows for highest danger/potential level for both players"""
  # Reuse winning_row functionality
  # Move duplicate logic to lower level function

def find_best_row(player, game):
  """Chooses coordinates with max value from assign_danger_level()"""

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑


"""STRATEGY NOTES on 3 x 3

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