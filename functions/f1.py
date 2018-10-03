"""Functions to be called from tic-tac-toe.main"""

from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes import Game, SpotTakenError

from functions import f2, f3, ai


def determine_next_player(game):
  """Chooses player and returns corresponding player number (`0` or `1`)."""
  # if players have an equal number of steps, round starter will play
  if len(game.steps[0]) == len(game.steps[1]):
    return (game.round-1)%2
  # else, player with less steps will play
  # TODO: simplify (`else: return index of shorter one`)
  elif len(game.steps[0]) < len(game.steps[1]):
    return 0
  else:
    return 1


def find_winning_row(player, game):
  """Returns coordinates of winning row, if found.
  Example: `[(0, 0), (0, 1), (0, 2)]` → corresponds to a1-a2-a3"""
  stop = game.winning_size-1
  shapes = {"ud": {"range_y": (0, game.board_size - stop),
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
        row_coordinates = [((x + shape["step_x"]*i), (y + shape["step_y"]*i))
                           for i in range(game.winning_size)]
        row_marks = [game.board[xy[1]][xy[0]] for xy in row_coordinates]
        would_win = [MARKS[player]]*game.winning_size
        if row_marks == would_win:
          return row_coordinates


def game_create():
  """Returns Game instance from load, else new."""
  try:
    game = f3.game_load()
  except FileNotFoundError:
    game = Game()
  return game


def game_handle_match_end(player, game):
  """Updates `winner` and `scores` based on what's up."""
  if game.winning_row:
    game.winner = player
    game.scores[player] += 1
  else:
    game.winner = 'tie'
  game.round += 1
  return game


def game_new_round(game):
  """Resets round variables unless game was loaded just now."""
  if not game.loaded_now:
    game.board = f2.generate_board(game.board_size)
    game.steps = [[], []]
    game.winner = None
  game.loaded_now = False
  return game


def game_welcome_setup(game):
  """Updates game rules & player names based on user input.
  Skipped if game was loaded just now."""
  f2.welcome_start(game.loaded_now)
  if not game.loaded_now:
    game.board_size = f2.get_board_size()
    game.winning_size = f2.get_winning_size(game.board_size)
    game.players = f2.get_player_names()
  f2.welcome_end(game.loaded_now)
  return game


def init_action(player, game):
  """Decides whether human or AI is coming up.
  Calls prompt_action() or ai_action() accordingly."""
  if ai.ai_in_players(player, game):
    ai.ai_action(player, game)
  else:
    f2.prompt_action(player, game)


def is_it_a_tie(steps, board_size):
  """Returns `True` if board is full"""
  if len(steps[0]) + len(steps[1]) == board_size**2:
  # TODO: rewrite to analyze board instead
    return True


def update_screen(player, game):
  """Clears screen. Prints scores, instructions and board if match is ongoing.
  If match ended, omits instructions and prints result."""
  system('clear')
  if game.winner == None:
    f2.print_scores(game.players, game.scores)
    if game.players[player].lower() != 'ai':
      print('', *INSTRUCTIONS, sep='\n')
    else:
      print('', *map(lambda x: colored(x, attrs=['dark']), INSTRUCTIONS), sep='\n') # AB: greyout (fancier)
      # print('\n'*(len(INSTRUCTIONS)+1))                                           # AB: whiteout (cleaner)
    f2.print_board(game)
    # TODO: move to prompt_action() and take print_board out of the if-else
    print(colored(f"\n{game.players[player]}", COLORS[player], attrs=['bold']) +
                   ", make your move: ", end='')
  else:
    print('\n'*(len(INSTRUCTIONS)+2))
    f2.print_board(game)
    # print_win(player, game)
    if game.winner in (0, 1):
      print(colored(f"\n{game.players[player]} wins in {len(game.steps[player])} "
                     "steps!", COLORS[player], attrs=['bold'])); sleep(WAIT)
    # print_tie(player, game)
    elif game.winner == 'tie':
      print(colored("\nIt's a tie!", attrs=['bold'])); sleep(WAIT)
    f2.print_scores(game.players, game.scores); sleep(WAIT)


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
  