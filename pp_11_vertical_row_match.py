# DON'T Trust user's Input
game = [
		[2,0,1],
		[2,1,0],
		[2,1,1],
	   ]

# len(game) = 3

# You can win Tic-Tac-Toe game by 4 ways
# 1) Horizontally - same values of all elements in a check
# 2) Vertically   - same values of elements of each check at same index. 
# 3) Diagonally   - same values at index[row=columns]
# 4) Inverse-Diagonally - index[col = row]

# def win(current_game):
# 	for row in game:
# 		if check.count(check[0]) == len(check):
# 			print("Winner")

for col in range(len(game)):
	check = []
	for row in game:
		check.append(row[col])

	if check.count(check[0]) == len(check):
		print("Winner")


# win(game)