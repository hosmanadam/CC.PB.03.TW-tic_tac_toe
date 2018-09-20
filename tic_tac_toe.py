from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle

from constants import *
import functions as f


def main():
  try:
    game = f.game_create()
    game = f.game_welcome_setup(game)
    wants_to_play = True
    while wants_to_play:
      game = f.game_new_round(game)
      while game.winner == None:
        for player in (0, 1):
          if f.is_wrong_player(player, game): continue
          f.update_screen(player, game)
          # f.prompt_action(player, game) # AI STUFF
          f.init_action(player, game)     # AI STUFF
          game.winning_row = f.find_winning_row(player, game)
          game.last_player = player
          if game.winning_row or f.is_it_a_tie(game.steps, game.board_size):
            game = f.game_handle_match_end(player, game)
            f.update_screen(player, game)
            wants_to_play = f.wants_rematch()
            break
    f.quit()
  except KeyboardInterrupt:
    print('')
    f.quit()


if __name__ == '__main__':
  main()