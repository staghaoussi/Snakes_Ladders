# The SL_Board class simulates a Snakes & Ladders board
 
class SL_Board:
	
	def __init__(self, width, snakes, ladders):
		# Assumes the board is square (width wide by width tall)
		# Paramter: snakes:  A list of integer tuples (head, tail), 
		#          where 1 <= head < tail <= width * width - 1
		# Parameter: ladders: A list of tuples (bottom, top), 
		#          where 1 <= bottom < top <= width * width - 1
		self.__width = width
		self.__length = width * width
		
		board = []
		#each square of the board is (intially) an empty list
		for count in range(1, width*width + 1):
			board.append([])
		
		#squares with snake heads or tails are appended with:
		#  Snake heads: list containing a string "S#T" where # is an integer
		#  Snake tails: a list: ["S#H" where # is an integer, location of the tail]
		snake_count = 1
		for snake in snakes:
			# Ensure Snake is on the board
			if 0 < snake[0] < self.__length and 0 < snake[1] < self.__length:
				#Ensure nothing else is there! 
				if len(board[snake[0]-1]) == 0 and len(board[snake[1]-1]) == 0:
					#head
					board[snake[0]-1].append( "S"+str(snake_count)+"H" )
					board[snake[0]-1].append(snake[1] ) #location of tail
					#tail
					board[snake[1]-1].append( "S"+str(snake_count)+"T")
					snake_count += 1


		#squares with ladder bottoms or tops are appended with:
		#  Ladder bottoms: a list: ["L#B" where # is an integer, location of the top]
		#  Ladder tops: a list: "L#T" where # is an integer
		ladder_count = 1
		for ladder in ladders:
			if 0 < ladder[0] < self.__length and 0 < ladder[1] < self.__length:
				#Ensure nothing else is there! 
				if len(board[ladder[0]-1]) == 0 and len(board[ladder[1]-1]) == 0:
					#bottom
					board[ladder[0]-1].append( "L"+str(ladder_count)+"B")
					board[ladder[0]-1].append(ladder[1] )
					#top
					board[ladder[1]-1].append( "L"+str(ladder_count)+"T" )
					ladder_count += 1
		#Create Board for the class		
		self.__board = board

		
	# get_length - accessor method
	# returns the length of the board (aka, the number on the last square)
	def get_length(self):
		return self.__length
	
	# is_snake - accessor method - Check if the square is the head of a snake
	# returns true if the square is the head of a snake
	def is_snake(self, index):
		if len(self.__board[index-1]) == 2 and self.__board[index-1][0].startswith("S"):
			#its a snake head
			return True
		else: 
			return False
			
	# get_snake_tail - an accessor method
	# parameter - index of a square that is the head of a snake
	# returns the index of the tail of the snake whose head is at the parameter
	def get_snake_tail(self, index):
		if self.is_snake(index):
			return self.__board[index-1][1]
		else: 
			# its not a snake, do nothing
			return index

	# is_ladder - accessor method: Checks if the square is bottom of a ladder
	# returns true if the square is the bottom of a ladder
	def is_ladder(self, index):
		if len(self.__board[index-1]) == 2  and self.__board[index-1][0].startswith("L"):
			#its a snake tail
			return True
		else: 
			return False
			
	# get_ladder_top - an accessor method
	# parameter - index of a square that is the bottom of a ladder
	# returns the index of the top of the ladder whose bottom is at the parameter
	def get_ladder_top(self, index):
		if self.is_ladder(index):
			return self.__board[index-1][1]
		else: 
			# its not a ladder, do nothing
			return index


	# one_square - accessor method
	# returns the value on one square of the board (specified by index)
	def one_square(self,index):
		return self.__board[index]

		
	#returns the board attributes, showing a text version of the board, 
	# all squares numbered 1 - length, except squares that represent the 
	#  head or tail of a snake or the top or bottom of a ladder. 
	def __str__(self):
		str_Value = "\n"
		
		#backward: ensures every second row output backward
		backward = False
		backCount = self.__width - 1
		for count in range(0,len(self.__board)):

			if backward:
				use = count + backCount
			else:
				use = count
			
			if len(self.__board[use]) == 0:
				# square has empty list, ie, no snake or ladder
				str_Value += str(use+1) + "\t"
			else :
				# square has either snake or ladder
				str_Value += self.__board[use][0] + "\t"
				
			# ends a line and ensures next line is output in opposite order
			if count % self.__width == self.__width-1:
				str_Value += "\n"
				if backward: 
					backward = False
				else: 
					backward = True
				backCount = self.__width - 1
			elif backward:
				backCount -= 2
				
		
		str_Value += "\n"
		return str_Value

#def main(): #This is a 'Test Harness', it simply tests the class. 
	#game = SL_Board(4, [(15,2), (14,7)], [(4, 12),(14,15),(7,13)] )
	#print(game)
	#print(game.self__board)
	
	#if game.is_snake(15):
		#print(game.get_snake_tail(15))
	#else:
		#print("No snake at 15")
#main()
