game = "I wanted to play this Game now"
print(id(game))


def gaming_params(input=0, row=0, col=0, just_display=False):
	global game
	game = "A small Game"
	print(id(game))
	print(game)  

	# print("     0  1  2")
	# if not just_display:
	# 	game[row][col] = input
	# for count, row in enumerate(game):
	# 	print(count, row)

print(game)
print(id(game))
gaming_params() # this will be executed according to sequence.
print(game)
print(id(game))

