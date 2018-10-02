"""All constants for Tic-tac-toe."""

from termcolor import colored

COLUMNS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Included whole ABC for error handling
COLORS = ['red', 'green']
MARKS = [colored('X', COLORS[0]), colored('O', COLORS[1])]
EMPTY = ' '
WAIT = 1.5
WELCOME = ("*** Hello and welcome to " + colored("Tic-tac-toe ", attrs=['bold'])
         + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***")

WELCOME_BACK = ("*** Welcome back to " + colored("Tic-tac-toe ", attrs=['bold'])
              + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***")

GOODBYE = ("\n*** Thanks for playing. " + colored("Goodbye!", attrs=['bold']) +
           " ***")

INSTRUCTIONS = ("Undo last step: 'u'",
                "Save game and exit: 's'",
                "Exit without saving: 'q'",
                colored("Place mark by entering its coordinates "
                        "(e.g. 'a1', 'c2'):\n", attrs=['bold']))

stop = game.winning_size-1
SHAPES = {"ud": {"range_y": (0, game.board_size - stop),
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
