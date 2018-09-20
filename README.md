###Tic-tac-toe v2.0 by 2heads

##Welcome...
To our little study project, now 2 weeks in development at Codecool Budapest.
Here's some info about the code to aid everyone (including us) in not messing it up.

##Standards

#Coordinates
...are stored in tuples as `(x, y)`.
Board indexing must be done as `board[y][x]` (notice reverse order).

#Function hierarchy
Functions are always called top-to-bottom, for example:
– `main()` may call functions defined in `f1`, `f2`, `f3`.
– functions in `f2` may only call functions in `f3`.
In other words, functions in the same file/module don't call each other, or ones above them.

A funcion may call functions more than 1 level below it.
  In this case, when the lower function has siblings (ones that are very similar in functionality, e.g. `game_load` and `game_save`), they all go to the lower level.

#Function order
Function definitions are listed alphabetically.

#Tagging
Code lines related to AI functionality are tagged `# AI stuff` for easy finding.