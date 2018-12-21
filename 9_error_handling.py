# DON'T Trust user's Input
game = [
		[0,0,0],
		[0,0,0],
		[0,0,0],
	   ]


def gaming_params(game_map, input=0, row=0, col=0, just_display=False):
	try:
		print("     0  1  2")
		if not just_display:
			game_map[row][col] = input
		for index, row in enumerate(game):
			print(index,row)

		return game_map
	except IndexError as e:
		print("You have entered value of row/column other than 0,1,2\n",e)
		# print("you have an error, please follow syntax and check logic")
	except Exception as e:
		print("Error is not caught, so General Exception is called!\n",e)
	finally :
		print("It will run compulsorily")
game = gaming_params(game, just_display=True)
game = gaming_params(gaming_params, input=1, row=3, col=1) 