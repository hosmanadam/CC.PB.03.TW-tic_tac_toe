# Tic-tac-toe v2.0 by 2heads

## Welcome...
To our little study project, now 2 weeks in development at Codecool Budapest.
Here's some info about the code to aid everyone (including us) in not messing it up.

## Standards

### Coordinates
...are stored in tuples as `(x, y)`.
Board indexing must be done as `board[y][x]` (notice reverse order).

### Players
Players are always represented as `0` or `1` in the game logic.
This number is used to index all player-related attributes of game instance.
Player names are only used for printing and to determine whether current player is AI.
Players alternate in starting rounds, regardless of who won in the previous one.
`Game.player` is the player currently in control.
`Game.last_player` is the player with the last mark on current board.
`Game.player` and `Game.last_player` can never be the same (disregarding that technically, after undo, you are the one who performed the last action, and will also perform the next).

### Function hierarchy (under review)
Functions are always called top-to-bottom, for example:
– `tic-tac-toe.main` may call functions defined in `f1`, `f2`, `f3`, `ai`.
– functions in `f2` may only call functions in `f3`, `ai`.
In other words, functions in the same file/module may **not** call each other, or ones above them.

A funcion may call functions more than 1 level below it.
In this case, when the lower function has siblings (ones that are very similar in functionality, e.g. `game_load` and `game_save`), they all go to the lower level.

### Function order
Function definitions are listed alphabetically.

### Tagging
...
