import random
import string

class Player:
	def __init__(self):
		self.__name = ''
		self.__symbol = ''
		self.__position = 1
		

	def set_name(self, name):
		self.__name = name

	def set_symbol(self):
		self.__symbol = random.choice(string.ascii_lowercase)
	def get_name(self):
		return self.__name
	def get_symbol(self):
		return self.__symbol
	def set_position(self, position):
		self.__position = position
	def inc_position(self, position):
		self.__position += position
	def get_position(self):
		return self.__position
	def __str__(self):
		string = 'name = '+self.__name +' symbol = ('+ self.__symbol + '): position = ' + str(self.__position)
		return string

