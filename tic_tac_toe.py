from os import remove, system
from sys import exit
from termcolor import colored
from time import sleep
import pickle


if __name__ == '__main__':
  def main():
    import data.variables as v
    import data.constants as c
    import functions.all as f
    try:
      system('clear')
      try:
        v.board_size, v.winning_size, v.players, v.scores, v.board, v.steps, current_player = f.game_load()
        print(c.WELCOME_BACK[0]); sleep(c.WAIT)
        print(c.WELCOME_BACK[1]); sleep(c.WAIT)
        from_load = True                                    # HACK 1
      except FileNotFoundError:
        print(c.WELCOME); sleep(c.WAIT)
        v.board_size, v.winning_size, v.players, v.scores, current_player = f.game_new()
        print("\nLet's begin..."); sleep(c.WAIT)
        from_load = False                                   # HACK 1
      wants_to_play = True
      while wants_to_play:
        if not from_load:                                   # HACK 1 - resets round variables if game is new, not loaded
          v.board = f.generate_board(c.EMPTY, v.board_size) # HACK 1
          v.steps = [[], []]                                # HACK 1
        from_load = False                                   # HACK 1
        winner = None
        while winner == None:
          for player in range(2):
            system('clear')
            if player == 0 and len(v.steps[0]) > len(v.steps[1]):
              continue # Makes loaded game start with next player
            f.print_scores(v.players, v.scores, c.COLORS); print('')
            print(c.INSTRUCTIONS)
            last_player = [x for x in (0, 1) if x != player][0]
            f.print_board(last_player, winner, v.board_size, c.COLUMNS, 
                          v.winning_row, v.board, v.steps)
            print(colored(f"\n{v.players[player]}", c.COLORS[player], attrs=['bold']) +
                           ", make your move: ", end='')
            f.prompt_action(player, c.COLUMNS, c.EMPTY, c.MARKS, v.board, v.steps,  # for place_mark()
                            c.GOODBYE, c.WAIT,                                       # for quit()
                            v.board_size, v.winning_size, v.players, v.scores,       # for game_save()
                            v.board, v.steps, current_player)                        # for game_save()
            v.winning_row = f.did_player_win(player, v.winning_size, v.board_size, v.board, c.MARKS)
            if v.winning_row:
              winner = player
              system('clear')
              print('\n'*5)
              f.print_board(last_player, winner, v.board_size, c.COLUMNS, 
                            v.winning_row, v.board, v.steps)
              print(colored(f"\n{v.players[player]} wins in {len(v.steps[player])} "
                             "steps!", c.COLORS[player], attrs=['bold'])); sleep(c.WAIT)
              v.scores[player] += 1
              f.print_scores(v.players, v.scores, c.COLORS); sleep(c.WAIT)
              wants_to_play = f.wants_rematch()
              break
            if f.is_it_a_tie(v.steps, v.board_size):
              winner = 'tie'                                                  # HACK 2 - duplicate of winning scenario
              system('clear')                                                 # HACK 2   w/ minor modifications
              print('\n'*5)                                                   # HACK 2
              f.print_board(last_player, winner, v.board_size, c.COLUMNS,     # HACK 2
                            v.winning_row, v.board, v.steps)                  # HACK 2
              print(colored("\nIt's a tie!", attrs=['bold'])); sleep(c.WAIT)  # HACK 2
              f.print_scores(v.players, v.scores, c.COLORS); sleep(c.WAIT)    # HACK 2
              wants_to_play = f.wants_rematch()                               # HACK 2
              break                                                           # HACK 2
      f.quit(c.GOODBYE, c.WAIT)
    except KeyboardInterrupt:
      print('')
      f.quit(c.GOODBYE, c.WAIT)

  main()