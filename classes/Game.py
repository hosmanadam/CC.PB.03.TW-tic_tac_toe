class Game:
  """Contains all game variables."""
  def __init__(self):
    # Fixed at `game_new()`
    self.board_size = None
    self.winning_size = None
    self.player_names = [None, None]
    # Updated after every match end
    self.scores = [0, 0]
    self.round = 1
    self.winner = None
    self.winning_row = [] # (x, y) coordinates (to be indexed as board[y][x])
    # Updated after every step
    self.board = []
    self.steps = []       # (x, y) coordinates (to be indexed as board[y][x])
    self.current_player = None
    self.last_player = None
    self.loaded_now = False
