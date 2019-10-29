#1
board = []

for i in range(8):
	board.append(["","","","","","","",""])

#2
temp = 0
for lists in board:
	if temp < 3:
		for i in range(len(lists)):
			lists[i] = 'r'
		
	elif temp >4:
		for i in range(len(lists)):
			lists[i] = 'b'
	
	temp += 1

dicty = {'A':0, 'B':1, 'C':2, 'D':3, 'D':4, 'E':5, 'F':6, 'G':7}

#4
while True:
	while True:
		#turn of black player
		player_black = input('Its your turn black (Enter quit to pass)')

		#conditions to check invalid moves
		cond1 = player_black[1] == player_black[4]#check if the move is straight
		cond2 = (board[dicty.get(player_black[0])][int(player_black[1])]) == 'r'#check if from position is of black
		cond3 = (board[dicty.get(player_black[0])][int(player_black[1])]) == ''#check if from position is empty
		
		if player_black == 'quit':
			break
		else:
			if cond1 == False and cond2 == False and cond3 == False:

				from_row_b = player_black[0]
				from_block_b = int(player_black[1])
				to_row_b = player_black[3]
				to_block_b = int(player_black[4])

				board[dicty.get(from_row_b)][from_block_b] = ''
				board[dicty.get(to_row_b)][to_block_b] = 'b'

				break
			else:
				print('Please enter a valid move')

	while True:	
		#turn of red player
		player_red = input('Its your turn red (Enter quit to pass)')

		#conditions to check invalid moves
		cond1 = player_red[1] != player_red[4]#check if the move is straight
		cond2 = (board[dicty.get(player_red[3])][int(player_red[4])]) == ''#check if to position is empty
		
		if player_red == 'quit':
			break
		else:
			if cond1 == True and cond2 == True:

				from_row_r = player_red[0]
				from_block_r = int(player_red[1])
				to_row_r = player_red[3]
				to_block_r = int(player_red[4])

				board[dicty.get(from_row_r)][from_block_r] = ''
				board[dicty.get(to_row_r)][to_block_r] = 'r'

				break
			else:
				print('Please Enter a valid move')



