game = [1,2,3]
print(id(game))

def gaming_params(input=0, row=0, col=0, just_display=False):
	game[0] = 100 
	print(id(game))

	print("Local scope value  ", game)  

	# print("     0  1  2")
	# if not just_display:
	# 	game[row][col] = input
	# for count, row in enumerate(game):
	# 	print(count, row)

print("Before calling func ", game)
print(id(game))
gaming_params() # this will be executed according to sequence.
print("after calling func ", game)
print(id(game))

