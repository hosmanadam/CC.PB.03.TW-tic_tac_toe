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
          if player == game.last_player:
            continue # Prevents loaded game from starting with last player
          f.update_screen(player, game)
          f.prompt_action(player, game)
          game.winning_row = f.find_winning_row(player, game)
          game.last_player = player

          if game.winning_row:
            # game = f.handle_win()
            game.winner = player
            game.scores[player] += 1

            system('clear')
            print('\n'*5)
            f.print_board(game)

            # print_win(player, game)
            print(colored(f"\n{game.players[player]} wins in {len(game.steps[player])} "
                            "steps!", COLORS[player], attrs=['bold'])); sleep(WAIT)


            f.print_scores(game.players, game.scores); sleep(WAIT)
            wants_to_play = f.wants_rematch()
            break

          # game = f.handle_tie()
          if f.is_it_a_tie(game.steps, game.board_size):
            game.winner = 'tie'

            system('clear')                                         # DUPLICATE
            print('\n'*5)                                           # DUPLICATE
            f.print_board(game)                                     # DUPLICATE

            print(colored("\nIt's a tie!", attrs=['bold'])); sleep(WAIT)

            f.print_scores(game.players, game.scores); sleep(WAIT)  # DUPLICATE
            wants_to_play = f.wants_rematch()                       # DUPLICATE
            break

    f.quit()
  except KeyboardInterrupt:
    print('')
    f.quit()


if __name__ == '__main__':
  main()