game = [
		[1,0,2],
		[0,1,0],
		[1,2,0],
	   ]

# len(game) = 3
# diags = (range(len(game)))
rev_diags = list(reversed(range(len(game)))) 
# reversed returns iterator not sequence of elements, 
# else throws error as object is not subscriptable

# for idx in range(len(game)):
# 	print(idx, rev_diags[idx])

# for col,row, in zip(diags,rev_diags):
	# print(row,col)


diags = [] 
for row,col in enumerate(rev_diags): # It started from index=2 upto index=0
	diags.append(game[row][col])

print(diags)
# print(rev_diags)



# for ix in range(len(game)):   # range works excluding last element/boundary
# 	diags.append(game[ix][ix])
# print("diags = ", diags)

# for i in reversed(range(len(game))):  # reversed starts at last element to 1st
# 	print(i)

# for ix in range(len(game) -1  ):
# 	rev_diags.append(game[len(game)-ix-1][ix-1])
# print("rev_diags = ", rev_diags)

# for col in range(len(game)):
# 	# diags = []
# 	# for row in game:
# 		# diags.append(row[col])

# 	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
# 		print("Winner")


