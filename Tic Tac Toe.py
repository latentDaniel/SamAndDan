#Tic Tac Toe Game

row1 = [1, 2, 3]	
row2 = [4, 5, 6]
row3 = [7, 8, 9]

gameBoard = [row1, row2, row3]

symbolX = 'X'
symbolO = 'O'

#######################
#Functions
#This function prints the game board
def printBoard():
	print 'Game Board:'
	print ' ' + str(row1[0]) + ' | ' + str(row1[1]) + ' | ' + str(row1[2])
	print ' ---------'
	print ' ' + str(row2[0]) + ' | ' + str(row2[1]) + ' | ' + str(row2[2])
	print ' ---------'
	print ' ' + str(row3[0]) + ' | ' + str(row3[1]) + ' | ' + str(row3[2])
	print ' '

#This function adds moves to the board	
def moves(symbol):
	move = raw_input()
	if move == '1':			#Change to make move == spot number
		row1[0] = symbol	#Add more of these in order to cover all of the board
	elif move == '2':
		row1[1] = symbol
	elif move == '3':
		row1[2] = symbol
	elif move == '4':
		row2[0] = symbol
	elif move == '5':
		row2[1] = symbol
	elif move == '6':
		row2[2] = symbol
	elif move == '7':
		row3[0] = symbol
	elif move == '8':
		row3[1] = symbol
	elif move == '9':
		row3[2] = symbol
	else:
		print 'You did not choose a valid space. Better luck next time.'	
	
def player1():
	printBoard()
	print 'Type the number of the spot that you would like to take.'
	print 'Player 1, what is your move?'
	moves(symbolX)

def player2():
	printBoard()
	print 'Type the number of the spot that you would like to take.'
	print 'Player 2, what is your move?'
	moves(symbolO)

#This function checks for empty spots
def gameEnd():
	x = 0
	y = 0
	
	while x < 3:
#		print gameBoard[x]
		
		while y < 3:
			testForInt = gameBoard[x][y]		#Tests gameboard for integers
#			print gameBoard[x][y]
			
			if type(testForInt) == int:		#If there is a number, return False
				return False
			else:	#If there is not a number, pass
				pass	
			y += 1
		
		x += 1
		y = 0
		
	return True

#This is a function to check for a winning play
def moveEnd(symbol): #True means game end. False means keep playing.
	if row1 == [symbol, symbol, symbol]:
		return True
	elif row2 == [symbol, symbol, symbol]:
		return True
	elif row3 == [symbol, symbol, symbol]:
		return True
	elif row1[0] == symbol and row2[0] == symbol and row3[0] == symbol:
		return True
	elif row1[1] == symbol and row2[1] == symbol and row3[1] == symbol:
		return True
	elif row1[2] == symbol and row2[2] == symbol and row3[2] == symbol:
		return True
	elif row1[0] == symbol and row2[1] == symbol and row3[2] == symbol:
		return True
	elif row1[2] == symbol and row2[1] == symbol and row3[0] == symbol:
		return True
	else:
		return False

#########################
#Program
print 'Welcome to Tic Tac Toe!'
print 'Player 1 is X'
print 'Player 2 is O'
print ' '

#While there are still ints on the board, or no one has won, keep playing
while True:
	player1()		#Player 1's turn
	if moveEnd(symbolX) == False and gameEnd() == False:		#If no one has won, and there are still playable spots, keep playing.
		pass
	elif moveEnd(symbolX) == False and gameEnd() == True:	#Looks for ints. If none, and no one has won, it is a tie game.
		print 'There was a tie...'
		break
	else:		#If player 1 has won, stop the loop
		print 'Player 1 wins!'
		break
	player2()
	if moveEnd(symbolO) == False and gameEnd() == False:		#If player 2 has not won yet, continue on
		pass
	elif moveEnd(symbol0) == False and gameEnd() == False:
		print 'There was a tie...'
		break
	else:		#If player 2 has won stop the loop
		print 'Player 2 wins!'
		break

printBoard()
