# Snakes_Ladders
To play game download all python files (Die.py, SL_Board.py, SL_Game.py, Player.py) and boardConfig.txt file.
Once all files are downloaded run SL_Game.py file to commence the game.
Use the following command in command prompt to start the game.

python SL_Game.py


Created a Python Snakes and Ladders game who uses 2-6 players. Used object oriented programming for each player.
Turns are automated, only input needed is number of players and player name. 



Information about the board. 

SNAKE TILE
if tile on board has an S, that means that the tile is a snake
if the tile is followed by an T it means that it is the snake tail tile
if the tile is followed by an H it means that it is the snake head tile

Number between letter S and T or H determines which snake it is.
ex: 
S1T corresponds to snake tail 1
S1H corresponds to snake head 1
ie they are the same snake

LADDER TILE
if the tile on the board has an L, that means the the tile is a ladder
if the tile is followed by an B it means that it is the ladder bottom tile
if the tile is followed by an T it means that it is the ladder top tile

Number between letter L and B or T determines which ladder it is.
ex: 
L2B corresponds to ladder bottom 2
L2T corresponds to latter top 2
ie they are the same ladder

example of board.

The board:

1       2       S1T     4       5       6
12      11      S2T     9       L2B     7
S3T     S1H     15      16      L1B     18
L3B     S2H     22      21      20      19
S4T     L3T     27      L1T     L2T     30
36      35      S4H     33      32      


To change the board layout, modify boardConfig.txt
