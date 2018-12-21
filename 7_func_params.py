game = [
		[0,0,0],
		[0,0,0],
		[0,0,0],
	   ]


def gaming_params(input=0, row=0, col=0, just_display=False):
	print("     0  1  2")
	if not just_display:
		game[row][col] = input
	for index, row in enumerate(game):
		print(index,row)


gaming_params(just_display=True)
gaming_params(input=1, row=2, col=1)