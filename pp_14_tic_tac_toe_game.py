import itertools

def win(current_game):

    def check_all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #Horizontal
    for row in game:
        print(row)
        if check_all_same(row):
            print("Horizontally")
            print(f"Player {row[0]} Won Horizontally ")
            return True

    # Diagonal
    diags = [] 
    for col,row in enumerate(reversed(range(len(game)))): # It started from index=2 upto index=0
        diags.append(game[row][col])
    if check_all_same(diags):
        print("Diagonally (/) ")
        print(f"Player {diags[0]} Won Reverse-Diagonally (/)")
        return True


    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if check_all_same(diags):
        print("Diagonally (\\)")
        print(f"Player {diags[0]} Won Diagonally (\\)")
        return True

    #Vertical
    for col in range(len(game)):
        check  = [] 
        for row in game:
            check.append(row[col])

        if check_all_same(check):
            print("Vertically")
            print(f"Player {check[0]} Won Vertically =")
            return True
    return False 
# win(game)


def gaming_params(game_map, input=0, row=0, col=0, just_display=False):
    try:
        if game[row][col] != 0:
            print("this position is occupied, please choose other")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][col] = input
        for index, row in enumerate(game):
            print(index,row)

        print("**********************************************************")
        return game_map, True
 
    except IndexError as e:
        print("You have entered value of row/column other than 0,1,2\n",e)
        # print("you have an error, please follow syntax and check logic")
        return  game_map, False
    except Exception as e:
        print("Error is not caught, so General Exception is called!\n",e)
        return  game_map, False
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
    game, _ = gaming_params(game, just_display = True) # before game starts
    player_choice = itertools.cycle([1,2])

    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player => {current_player}")
        played = False

        while not played:
            row_choice = int(input("In which Row you wanted to enter value(0,1,2)?=> "))
            column_choice = int(input("In which Column you wanted to enter value ? => "))
            game , played = gaming_params(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("Do you want to Play it Again?")
            if again.lower() == 'y':
                print("Restarting Game")
                play = True
            else:
                print("Okay, Bye. Terminating game...")
                play = False
;