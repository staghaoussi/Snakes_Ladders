import Die
import SL_Board
from Player import Player

def main():
	# setting up dice
	dice = Die.Die()

	# getting number of players
	number_players = 0
	try:
		number_players = int(input("Enter number of players between 2-6: "))
		
		# handling the case of invalid player number
		if(number_players>6 or number_players<2):
			raise Exception("Invalid input of number of players")
	# handling case of input not being integer
	except ValueError:
		print("Invalid input, must be integer")

	# creating players
	arr_players = [Player() for i in range(number_players)]
	
	#setting names and symbols
	for player_number in range (1,number_players+1):
		name = input("Player %d enter your name: " %(player_number))
		arr_players[player_number-1].set_name(name)
		arr_players[player_number-1].set_symbol()
		
	
	# making sure all players have different symbols
	for player in arr_players:
		#create list of symbols
		symbol_list = [player.get_symbol() for player in arr_players]
		#check if current player's symbol is in list more than once
		occurences = symbol_list.count(player.get_symbol())
		if occurences >1:
			while(symbol_list.count(player.get_symbol() == occurences)):
			#keep resetting current player symbol until it is different
				player.set_symbol()
	
		
	
	
	# printing board and players before starting the game
	board = boardData()
	print('\n\nSNAKES AND LADDERS\n')
	print('The board:')
	print(board)
	for player_number in range(1,number_players+1):
		print("Player %d = " %(player_number),arr_players[player_number-1])
	turn = 1
	#checking if any of the players positions have reached the last tile on the board
	while(all(player.get_position()!=board.get_length() for player in arr_players)):\
		# loop for all the players turn
		print("\n Turn %d" % turn)
		for player in arr_players:
			dice.throw()
			dice_number = dice.get_faceUp()

			player.inc_position(dice_number)
			
			if player.get_position() > board.get_length():
				player.set_position(board.get_length())
			elif board.is_snake(player.get_position()):
				player.set_position(board.get_snake_tail(player.get_position()))
			elif board.is_ladder(player.get_position()):
				player.set_position(board.get_ladder_top(player.get_position()))
			print(player)
			
			if player.get_position() == board.get_length():
				print('\nThe Winner is', player.get_name())
				break
		turn += 1


	
	

#Add and document suitable functions

#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()