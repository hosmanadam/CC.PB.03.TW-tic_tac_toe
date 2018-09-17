from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle

from data.constants import *
import functions.all as f


class Game:
  def __init__(self):
    # Fixed at new game start 
    self.board_size = f.get_board_size()
    self.winning_size = f.get_winning_size(self.board_size)
    self.players = f.get_player_names()
    # Updated after every win
    self.scores = [0, 0]
    self.winner = None
    self.winning_row = [] # (x, y) coordinates (to be indexed as board[y][x])
    # Updated after every step
    self.board = []
    self.steps = []       # (x, y) coordinates (to be indexed as board[y][x])


if __name__ == '__main__':
  def main():
    try:
      system('clear')
      try:
        g = f.game_load()
        print(WELCOME_BACK[0]); sleep(WAIT)
        print(WELCOME_BACK[1]); sleep(WAIT)
        from_load = True                           # HACK 1
      except FileNotFoundError:
        print(WELCOME); sleep(WAIT)
        g = Game()
        print("\nLet's begin..."); sleep(WAIT)
        from_load = False                          # HACK 1
      wants_to_play = True
      while wants_to_play:
        if not from_load:                          # HACK 1 - resets round variables if game is new, not loaded
          g.board = f.generate_board(g.board_size) # HACK 1 - TODO: implement more elegant reset() method
          g.steps = [[], []]                       # HACK 1
        from_load = False                          # HACK 1
        g.winner = None
        while g.winner == None:
          for player in range(2):
            system('clear')
            if player == 0 and len(g.steps[0]) > len(g.steps[1]):
              continue # Makes loaded game start with next player
            f.print_scores(g.players, g.scores); print('')
            print(INSTRUCTIONS)
            last_player = [x for x in (0, 1) if x != player][0]
            f.print_board(last_player, g)
            print(colored(f"\n{g.players[player]}", COLORS[player], attrs=['bold']) +
                           ", make your move: ", end='')
            f.prompt_action(player, g)
            g.winning_row = f.did_player_win(player, g)
            if g.winning_row:
              g.winner = player
              system('clear')
              print('\n'*5)
              f.print_board(last_player, g)
              print(colored(f"\n{g.players[player]} wins in {len(g.steps[player])} "
                             "steps!", COLORS[player], attrs=['bold'])); sleep(WAIT)
              g.scores[player] += 1
              f.print_scores(g.players, g.scores); sleep(WAIT)
              wants_to_play = f.wants_rematch()
              break
            if f.is_it_a_tie(g.steps, g.board_size):
              g.winner = 'tie'                                                # HACK 2 - duplicate of winning scenario
              system('clear')                                                 # HACK 2   w/ minor modifications
              print('\n'*5)                                                   # HACK 2
              f.print_board(last_player, g)                                   # HACK 2
              print(colored("\nIt's a tie!", attrs=['bold'])); sleep(WAIT)    # HACK 2
              f.print_scores(g.players, g.scores); sleep(WAIT)                # HACK 2
              wants_to_play = f.wants_rematch()                               # HACK 2
              break                                                           # HACK 2
      f.quit()
    except KeyboardInterrupt:
      print('')
      f.quit()

  main()