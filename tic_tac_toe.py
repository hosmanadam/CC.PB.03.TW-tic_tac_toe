# def generate_board():
#   """Readable version"""
#   board = [[char for char in COLUMNS[:board_size + 1]]]
#   for i in range(board_size):
#     row = [str(i+1)] + [' ']*board_size
#     board.append(row)
#   return board

def generate_board():
  """Short version"""
  return ([[char for char in COLUMNS[:board_size + 1]]]
         + [[str(i+1)] + [' ']*board_size for i in range(board_size)])

def print_board():
  print(100*'\n')
  for row in board:
    print(row)

# def print_board():
#   print(100*'\n')
#   for row in board:
#     for char in row:
#       print(char, end='')
#     print('')
    
def placement(player):
  coordinates = input(f"{players[player]}, enter your coordinates (e.g. a1, c2): ")
  row = int(coordinates[1:])
  column = COLUMNS.index(coordinates[0].upper())
  if board[row][column] == " ":
    board[row][column] = MARKS[player]
  else:
    print("That's spot is already taken.")
    placement(player)

def did_player_win(player):
  stop = to_win-1
  shapes = {
            "ud":   {"range_y": (1, board_size+1 - stop),
                     "range_x": board_size+1,
                     "step_y": 1,
                     "step_x": 0},

            "lr":   {"range_y": (1, board_size+1),
                     "range_x": board_size+1 - stop,
                     "step_y": 0,
                     "step_x": 1},

            "ullr": {"range_y": (1, board_size+1 - stop),
                     "range_x": board_size+1 - stop,
                     "step_y": 1,
                     "step_x": 1},

            "urll": {"range_y": (3, board_size+1 - stop),
                     "range_x": board_size+1 - stop,
                     "step_y": -1,
                     "step_x": 1}
  }
  
  for shape in shapes.values():
    for y in range(*shape["range_y"]):
      for x in range(shape["range_x"]):
        if [board[y + shape["step_y"]*i][x + shape["step_x"]*i] for i in range(to_win)] == [MARKS[player]]*to_win:
          return True
  
def get_player_names():
  return [input("Enter Player 1 name: "), input("Enter Player 2 name: ")]


print(100*'\n')
COLUMNS = ' ABCDEFGHIJ'
# COLUMNS = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# ROWS = [' ', '1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', '10 ']
MARKS = 'XO'
board_size = int(input("What size board (from 3-10) would you like to play on? ")) # Actual playing area (1 smaller than matrix)
to_win = int(input("How many marks in a row to win? "))
players = get_player_names()

board = []
scores = [0, 0]
wants_to_play = True

while wants_to_play:
  board = generate_board()
  print_board()
  winner = None
  while not winner:
    for player in range(2):
      placement(player)
      print_board()
      if did_player_win(player):
        print(f"{players[player]} wins!")
        winner = players[player]
        scores[player] += 1
        print(scores)
        if input("Would you like to play again? (y/n) ").lower()[0] == "n":
          wants_to_play = False
        break
      
