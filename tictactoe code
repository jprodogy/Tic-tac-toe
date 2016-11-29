Jeffrey Boudreaux and Quentin Polk
board = [['|', ' ','|', ' ','|', ' ','|'], ['|', ' ','|', ' ','|', ' ','|'], ['|', ' ','|', ' ','|', ' ','|']]

def clear_screen():
    # Clear the screen by printing a bunch of empty lines
    for line in range(50):
        print()
#Jeffrey
def board_creator(new_board):
	cold = ''
	for row in new_board:
		print(''.join(row))
#Quentin
def gamer_1(coordinate):
	if Player_1 == '1,1':
		board[0][1] = 'X'
		return board_creator(board)
	elif Player_1 == '1,2':
		board[0][3] = 'X'
		return board_creator(board)
	elif Player_1 == '1,3':
		board[0][5] = 'X'
		return board_creator(board)
	elif Player_1 == '2,1':
		board[1][1] = 'X'
		return board_creator(board)
	elif Player_1 == '2,2':
		board[1][3] = 'X'
		return board_creator(board)
	elif Player_1 == '2,3':
		board[1][5] = 'X'
		return board_creator(board)
	elif Player_1 == '3,1':
		board[2][1] = 'X'
		return board_creator(board)
	elif Player_1 == '3,2':
		board[2][3] = 'X'
		return board_creator(board)
	elif Player_1 == '3,3':
		board[2][5] = 'X'
		return board_creator(board)
	else:
		return 'Invalid move try again'
#Quentin
def gamer_2(coordinate):
	if Player_2 == '1,1':
		board[0][1] = 'O'
		return board_creator(board)
	elif Player_2 == '1,2':
		board[0][3] = 'O'
		return board_creator(board)
	elif Player_2 == '1,3':
		board[0][5] = 'O'
		return board_creator(board)
	elif Player_2 == '2,1':
		board[1][1] = 'O'
		return board_creator(board)
	elif Player_2 == '2,2':
		board[1][3] = 'O'
		return board_creator(board)
	elif Player_2 == '2,3':
		board[1][5] = 'O'
		return board_creator(board)
	elif Player_2 == '3,1':
		board[2][1] = 'O'
		return board_creator(board)
	elif Player_2 == '3,2':
		board[2][3] = 'O'
		return board_creator(board)
	elif Player_2 == '3,3':
		board[2][5] = 'O'
		return board_creator(board)
	else:
		return 'Invalid move try again'
#Jeffrey
def game_winner(coordinate):
	if coordinate[0][1] == coordinate[0][3] and coordinate[0][1] == coordinate[0][5] and (coordinate[0][1] == 'X' or coordinate[0][1] == 'O'):
		return True
	elif coordinate[1][1] == coordinate[1][3] and coordinate[1][1] == coordinate[1][5] and (coordinate[1][1] == 'X' or coordinate[1][1] == 'O'):
		return True
	elif coordinate[2][1] == coordinate[2][3] and coordinate[2][1] == coordinate[2][5] and (coordinate[2][1] == 'X' or coordinate[2][1] == 'O'):
		return True
	elif coordinate[0][1] == coordinate[1][3] and coordinate[0][1] == coordinate[2][5] and (coordinate[0][1] == 'X' or coordinate[0][1] == 'O'):
		return True
	elif coordinate[0][1] == coordinate[1][1] and coordinate[0][1] == coordinate[2][1] and (coordinate[0][1] == 'X' or coordinate[0][1] == 'O'):
		return True
	elif coordinate[0][5] == coordinate[1][3] and coordinate[0][5] == coordinate[2][1] and (coordinate[0][5] == 'X' or coordinate[0][5] == 'O'):
		return True
	elif coordinate[0][3] == coordinate[1][3] and coordinate[0][3] == coordinate[2][3] and (coordinate[0][3] == 'X' or coordinate[0][3] == 'O'):
		return True
	elif coordinate[0][5] == coordinate[1][5] and coordinate[0][5] == coordinate[2][5] and (coordinate[0][5] == 'X' or coordinate[0][5] == 'O'):
		return True
#Jeffrey
print(board_creator(board))
game = False
gamers = 1
while game == False:
	while gamers == 1:
		Player_1 = input('what move would you like to take?')
		print(gamer_1(Player_1))
		if game_winner(board) == True:
			print('X is winner')
			game = True
			gamers += 10
		gamers += 1
	while gamers == 2:
		Player_2 = input('what move would you like to take?')
		print(gamer_2(Player_2))
		if game_winner(board) == True:
			print('O is winner')
			game = True
			gamers += 10
		gamers -= 1







