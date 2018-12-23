import itertools

game = [
		[1,2,0],
		[0,2,1],
		[1,2,1],
	   ]

# len(game) = 3

def win(current_game):
	#Horizontal
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0 :
			print("Horizontally")
			print(f"Player {row[0]} Won Horizontally ")

	# Diagonal
	diags = [] 
	for col,row in enumerate(reversed(range(len(game)))): # It started from index=2 upto index=0
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:

		print("Diagonally (/) ")
		print(f"Player {diags[0]} Reverse-Diagonally (/)")

	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print("Diagonally (\\)")
		print(f"Player {diags[0]} Diagonally (\\)")

	#Vertical
	for col in range(len(game)):
		check  = [] 
		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0:
			print("Vertically")
			print(f"Player {check[0]} Vertically =")

# win(game)


def gaming_params(game_map, input=0, row=0, col=0, just_display=False):
	try:
		print("   0  1  2")
		if not just_display:
			game_map[row][col] = input
		for index, row in enumerate(game):
			print(index,row)

		print("**********************************************************")
		return game_map

	except IndexError as e:
		print("You have entered value of row/column other than 0,1,2\n",e)
		# print("you have an error, please follow syntax and check logic")
	except Exception as e:
		print("Error is not caught, so General Exception is called!\n",e)
	# finally :
		# print("This block of code will run compulsorily")

play = True
players = [1,2]

while play:
	print("************* Game is started newly!! ***************")
	game = [[0,0,0],
			[0,0,0],
			[0,0,0]]

	game_won = False
	game = gaming_params(game, just_display = True) # before game starts
	player_choice = itertools.cycle([1,2])


	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player => {current_player}")
		row_choice = int(input("In which Row you wanted to enter value(0,1,2)?=> "))
		column_choice = int(input("In which Column you wanted to enter value ? => "))
		game = gaming_params(game, current_player, row_choice, column_choice)

# game = gaming_params(game, just_display=True)
# game = gaming_params(game, input=2, row=1, col=1) 