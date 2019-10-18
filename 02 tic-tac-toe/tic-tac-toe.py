# game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
#
#
# def game_board(game_map, player=0, row=0, column=0, just_display=False):
#     try:
#         print("   a  b  c")
#         if not just_display:
#             game_map[row][column] = player
#         for count, row in enumerate(game_map):
#             print(count, row)
#         return game_map
#     except IndexError as e:
#         print("Error: make sure you input row/column as 0, 1 or 2?", e)
#     except Exception as e:
#         print("Something went very wrong,", e)
#
#
# game = game_board(game, just_display=True)
# game = game_board(game, 1, 2, 1)


# game = [[1, 0, 1], [0, 0, 0], [2, 2, 0], ]
#
#
# def win(current_game):
#     for row in game:
#         if row.count(row[0]) == len(row) and row[0] != 0:
#             print("winner!")
#
#
# win(game)


# game = [[2, 0, 1], [0, 0, 1], [2, 2, 1], ]
#
# for col in range(len(game)):
#     check = []
#
#     for row in game:
#         check.append(row[col])
#
#     if check.count(check[0]) == len(check) and check[0] != 0:
#         print("winner!")


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












