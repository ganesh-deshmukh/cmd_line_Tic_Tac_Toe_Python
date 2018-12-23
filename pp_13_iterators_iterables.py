game = [
        [1,2,1],
        [1,0,0],
        [1,2,1],
       ]

# len(game) = 3

def win(current_game):
    #Horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0 :
            print("Horizontally")
            # print(f"Player {row[0]} Won Horizontally ")

    # Diagonal
    diags = [] 
    for col,row in enumerate(reversed(range(len(game)))): # It started from index=2 upto index=0
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:

        print("Diagonally (/) ")
        # print(f"Player {diags[0]} Reverse-Diagonally (/)")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Diagonally (\\)")
        # print(f"Player {diags[0]} Diagonally (\\)")

    #Vertical
    for col in range(len(game)):
        check  = [] 
        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Vertically")
            # print(f"Player {row[0]} Vertically (|)")


win(game)

# # print("game is = ", game)
# for index, row in game:
#   print()
# print("diags is  ", diags)
# print("reversed(range(len(game))) ",reversed(range(len(game))))
