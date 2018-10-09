"""Main module for Tic-tac-toe"""

from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle
import random

from constants import *
from classes.Game import Game
from classes.SpotTakenError import SpotTakenError

from functions import f1, f2, f3, ai


def main():
  try:
    game = f1.game_create()
    game = f1.game_welcome_setup(game)
    wants_to_play = True
    while wants_to_play:
      game = f1.game_new_round(game)
      while game.winner == None:
        game.player, game.last_player = f1.determine_players(game)
        f1.update_screen(game)
        f1.init_action(game)
        game.winning_row = f1.find_winning_row(game)
        if game.winning_row or f1.is_it_a_tie(game.steps, game.board_size):
          game = f1.game_handle_match_end(game)
          f1.update_screen(game)
          wants_to_play = f1.wants_rematch()
          break
    f3.quit()
  except KeyboardInterrupt:
    print('')
    f3.quit()


if __name__ == '__main__':
  main()
