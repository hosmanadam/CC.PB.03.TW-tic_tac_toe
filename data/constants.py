"""All constants for Tic-tac-toe."""

from termcolor import colored

COLUMNS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Included whole ABC for error handling
COLORS = ['red', 'green']
MARKS = [colored('X', COLORS[0]), colored('O', COLORS[1])]
EMPTY = ' '
WAIT = 1.5
WELCOME = ("*** Hello and welcome to " + colored("Tic-tac-toe ", attrs=['bold'])
        + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***")

WELCOME_BACK = ["*** Welcome back to " + colored("Tic-tac-toe ", attrs=['bold'])
              + "by " + colored("2heads", 'blue', attrs=['bold']) + "! ***",
                "Continuing from where you left off..."]

GOODBYE = ("\n*** Thanks for playing. " + colored("Goodbye!", attrs=['bold']) +
          " ***")

INSTRUCTIONS = ("Save game and exit: 's'\n"
                "Exit without saving: 'q'\n" +
                colored("Place mark by entering its coordinates "
                        "(e.g. 'a1', 'c2'):\n", attrs=['bold']))