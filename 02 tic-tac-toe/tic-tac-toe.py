import itertools


game = [[1, 0, 2], [1, 1, 2], [2, 2, 1], ]


def win(current_game):

    # horizontal
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally")

    # diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/)")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\)")

    # vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)
    except Exception as e:
        print("Something went very wrong,", e)


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)











#game = game_board(game, just_display=True)
#game = game_board(game, 1, 2, 1)



# game = [[1, 0, 1], [0, 0, 0], [2, 2, 0], ]
#
#

# game = [[2, 0, 1], [0, 0, 1], [2, 2, 1], ]
#



# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1], ]

# if game[0][0] == game[1][1] == game[2][2]:
#     print("winner!")
# if game[2][0] == game[1][1] == game[0][2]:
#     print("winner!")


# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1], ]
#
# diags = []
# for ix in range(len(game)):
#     diags.append(game[ix][ix])
# print(diags)


# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1], ]
#
# for i in reversed(range(len(game))):
#     print(i)


# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1], ]
#
# cols = list(reversed(range(len(game))))
# rows = range(len(game))
#
# for idx in rows:
#     print(idx, cols[idx])


# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1], ]
#
# cols = reversed(range(len(game)))
# rows = range(len(game))
#
# for col, row in zip(cols, rows):
#     print(col, row)


# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]
#
# for col, row in enumerate(reversed(range(len(game)))):
#     print(col, row)



# game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]
#
# diags = []
# for col, row in enumerate(reversed(range(len(game)))):
#     diags.append(game[row][col])
#
# print(diags)





# players = [1, 0]
# choice = 1
# for i in range(10):
#     current_player = choice
#     print(current_player)
#     choice = players[choice]


# import itertools
#
# player_choice = itertools.cycle([1, 2])
#
# for i in range(10):
#     print(next(player_choice))






