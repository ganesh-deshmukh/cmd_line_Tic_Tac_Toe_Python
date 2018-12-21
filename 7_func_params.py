game = [
		[0,0,0],
		[0,0,0],
		[0,0,0],
	   ]


def gaming_params(game_map, input=0, row=0, col=0, just_display=False):
	print("     0  1  2")
	if not just_display:
		game_map[row][col] = input
	for index, row in enumerate(game):
		print(index,row)

	return game_map


game = gaming_params(game, just_display=True)
game = gaming_params(game, input=1, row=2, col=1)