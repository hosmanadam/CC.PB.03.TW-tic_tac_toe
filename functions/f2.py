"""Functions to be called from functions.f1 or above"""

from os import remove, system
from sys import exit, stdout
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes import Game, SpotTakenError

from functions import f3


# AI stuff
def ai_action(player, game):
  """Prints AI 'thinking process' and places mark in random empty spot."""
  possibilities = f3.find_empty_coordinates(game)
  target = random.choice(possibilities)
  sleep(WAIT/2)
  for i in range(3):
    print('.', end=''); stdout.flush(); sleep(WAIT/2)
  print(f" {COLUMNS[target[0]].lower()}", end=''); stdout.flush(); sleep(WAIT/10)
  print(target[1]+1, end=''); stdout.flush(); sleep(WAIT/3)
  f3.place_mark(target, player, game)


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


def print_board(game):
  """Prints formatted board with headers, padding and pointer arrows added in appropriate places."""
  f3.print_column_headers(game.board_size)
  f3.print_rows(game)
  f3.print_column_headers(game.board_size)


def print_scores(players, scores):
  """Prints current scores in one line."""
  print(f"{players[0]}: " +
        colored(f"{scores[0]}", COLORS[0]) +
        f" - {players[1]}: " +
        colored(f"{scores[1]}", COLORS[1]))


def prompt_action(player, game, prompt=''):
  """Asks user to input coordinates. Handles 3 input cases (plus errors):
  (1) `'s'` → `save()`
  (2) `'q'` → `quit()`
  (3) coordinates → `place_mark()`"""
  try:
    action = input(prompt)
    if action.lower() == 's':
      f3.game_save(game); sleep(WAIT/2)
      f3.quit()
    elif action.lower() == 'q':
      f3.quit()
    else:
      row = int(action[1:])-1
      column = COLUMNS.index(action[0].upper())
      coordinates = (column, row)
      f3.place_mark(coordinates, player, game)
  except IndexError:
    prompt_action(player, game,
                  prompt="Coordinates out of range. Try again: ")
  except ValueError:
    prompt_action(player, game,
                  prompt="Incorrectly formatted coordinates. Try again: ")
  except SpotTakenError:
    prompt_action(player, game,
                  prompt="That spot is already taken. Try again: ")


def welcome_start(loaded_now):
  """Prints `WELCOME` message, or `WELCOME_BACK` when continuing saved game."""
  system('clear')
  if loaded_now:
    print(WELCOME_BACK); sleep(WAIT)
  else:
    print(WELCOME); sleep(WAIT)


def welcome_end(loaded_now):
  """Prints a bit of encouragement after setup is complete."""
  if loaded_now:
    print("\nContinuing from where you left off..."); sleep(WAIT)
  else:
    print("\nLet's begin..."); sleep(WAIT)