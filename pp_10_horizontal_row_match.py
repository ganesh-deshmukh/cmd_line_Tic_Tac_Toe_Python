# DON'T Trust user's Input
game = [
		[1,0,1],
		[0,1,0],
		[1,1,1],
	   ]
# You can win Tic-Tac-Toe game by 4 ways
# 1) Horizontally
# 2) Vertically
# 3) Diagonally 
# 4) Inverse-Diagonally

def win(current_game):
	for row in game:
		print("for row =", row)
		# all_match = True
		# for item in row:
		# 	# print("if( " + item + " !== " + row[0] + " )")
		# 	print(item,row)
		# 	if item != row[0]:
		# 		all_match= False

		# if all_match:
		# 	print("Winner")

		if row.count(row[0]) == len(row):
			print("Winner")

win(game)