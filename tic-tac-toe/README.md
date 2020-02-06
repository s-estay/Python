# tic tac toe game

## 018
Final:
```python
import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True

    # diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    # vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically")
            return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is ocupado! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong,", e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer")
                play = False
```

## 017
Beta:
```python
import itertools

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

```

## 016
Iterable: a thing we can iterate over.  
Iterator: a special object with next() method.  
Further explanation [here](https://youtu.be/au8xkSQW1kE?start=1362).

## 015
Iterate between players 1 and 2. We first iterate between 0 and 1:
```python
players = [1, 0]
choice = 1

for i in range(10):
    current_player = choice
    print(current_player)
    choice = players[choice]
```
Prints:
```
1
0
1
0
1
0
1
0
1
0
```
Then simply add 1 to iterate between 1 and 2:
```python
players = [1, 0]
choice = 1

for i in range(10):
    current_player = choice + 1
    print(current_player)
    choice = players[choice]
```
If we want to achieve the same result in a more condensed way, we can use `itertools` to iterate between two values in a list:
```python
import itertools

player_choice = itertools.cycle([1, 2])

for i in range(10):
    print(next(player_choice))
```

## 014
Bringing things together. Print what kind of winner using [f-Strings](https://realpython.com/python-f-strings/):
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

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

win(game)
```
To check an horizontal win use: `game = [[1, 0, 2], [2, 2, 2], [1, 2, 1], ]`. To check an vertical win use: `game = [[1, 0, 2], [1, 2, 2], [1, 2, 1], ]`. To check a vertical win use: `game = [[1, 0, 2], [1, 1, 2], [2, 2, 1], ]`.

## 013d
Diagonal winner. The following is a hardcoded solution to understand the pattern that results in a diagonal win:
```python
game = [[2, 0, 2], [1, 2, 0], [2, 2, 1]]

if game[0][0] == game[1][1] == game[2][2]:
    print("winner!")
if game[2][0] == game[1][1] == game[0][2]:
    print("winner!")
```
Prints:
```
winner!
```
Check left-to-right diagonal win, dynamically:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)
```
Prints:
```
[1, 1, 1]
```
To check right-to-left diagonal win, dynamically, we will use built-in function `reversed`:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

for i in reversed(range(len(game))):
    print(i)
```
Prints:
```
2
1
0
```
Create iterable elements **cols** and **rows**. Observe that `reverse` returns an iterator, not a sequence, so we need to converted it to a list:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

cols = list(reversed(range(len(game))))
rows = range(len(game))

for idx in rows:
    print(idx, cols[idx])
```
Prints:
```
0 2
1 1
2 0
```
We get the same result with the built-in function `zip`, which make an iterator that aggregates elements from each of the iterables. Observe that we don't need to convert reversed **cols** to a list when using `zip`:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

cols = reversed(range(len(game)))
rows = range(len(game))

for col, row in zip(cols, rows):
    print(col, row)
```
Prints:
```
0 2
1 1
2 0
```
Another way to get the same result (writing a lot less code) is by using built-in function `enumerate`:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

for col, row in enumerate(reversed(range(len(game)))):
    print(col, row)
```
Prints:
```
0 2
1 1
2 0
```
Finally, right-to-left diagonal is given by:
```python
game = [[1, 0, 2], [1, 1, 0], [2, 2, 1]]

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

print(diags)
```
Prints:
```
[2, 1, 2]
```

## 013c
Vertical winner:
```python
game = [[2, 0, 1], [2, 0, 0], [2, 2, 0], ]

for row in game:
    print(row[0])
```
Prints:
```
2
2
2
```
Similarly to [013b](https://github.com/s-estay/Python/tree/master/02%20tic-tac-toe#013b), we use `count` to return he number of times the row's first element appears in **check**. This value is compared to the length of **check**, a list that was created using `apend`, effectively creating a row out of a column:
```python
game = [[2, 0, 1], [2, 0, 0], [2, 2, 0], ]

check = []

for row in game:
    check.append(row[0])

if check.count(check[0]) == len(check) and check[0] != 0:
    print("winner!")
```
Prints:
```
winner!
```
Observe that the previous code only checks the first column. In order to go through the entire board we do like this:
```python
game = [[2, 0, 1], [0, 0, 1], [2, 2, 1], ]

columns = [0, 1, 2]

for col in columns:
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("winner!")
```
Prints:
```
winner!
```
This solution works but the number of columns are hardcoded. A better way is to use `range` which returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. So we change the outer for-loop to:
```python
game = [[2, 0, 1], [0, 0, 1], [2, 2, 1], ]

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("winner!")
```
Prints:
```
winner!
```
- [Python list count() method](https://www.w3schools.com/python/ref_list_count.asp)
- [Python range() function](https://www.w3schools.com/python/ref_func_range.asp)

## 013b
Horizontal winner:
```python
game = [[1, 1, 1], [0, 2, 0], [2, 2, 0], ]

def win(current_game):
    for row in game:
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        if col1 == col2 == col3:
            print("winner!")

win(game)
```
Prints:
```
winner!
```
This works but it's hardcoded. The right way to do it is doing it dynamically (and with less code) so the same code works for different board sizes. In the following example we will use the built-in functions `count` to count the number of appearances of the row's first element and compare it against the length of the row using `len`:
```python
game = [[1, 1, 1], [0, 2, 0], [2, 2, 0], ]

def win(current_game):
    for row in game:
        if row.count(row[0]) == len(row):
            print("winner!")

win(game)
```
Prints:
```
winner!
```
A final detail: due to the fact an empty box is signified with a `0` and player 1 and 2 play using `1` and `2` respectively, a row only consisting of `0` doesn't give a horizontal win and so we add:
```python   
game = [[1, 0, 1], [0, 0, 0], [2, 2, 0], ]

def win(current_game):
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner!")

win(game)
```
Prints nothing.

## 013a
You can win a tic tac toe game:
- horizontally
- vertically
- diagonally

## 012e
There're many more error handling options: `try`, `except`, `else`, `finally`, `raise`, etc.
 
## 012d
What if we pass a wrong argument to a function? In this example **game_board** instead of **game**:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)

game = game_board(game, just_display=True)
game = game_board(game_board, 1, 2, 1)
```
Prints:
```
TypeError: 'function' object is not subscriptable
```
To solve this error we can add a general exception:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)
    except Exception as e:
        print("Something went very wrong,", e)

game = game_board(game, just_display=True)
game = game_board(game_board, 1, 2, 1)
```
Prints:
```
Something went very wrong, 'function' object is not subscriptable
```

## 012c
Since we know that is was an **IndexError**, we can specify the exception:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)

game = game_board(game, just_display=True)
game = game_board(game, 1, 3, 1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
Error: make sure you input row/column as 0, 1 or 2? list index out of range
```

## 012b
Try and except statements.
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except:
        print("something went wrong!")

game = game_board(game, just_display=True)
game = game_board(game, 1, 3, 1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
something went wrong!
```
Observe that we haven't actually solved the problem.

## 012a
Error handling: when user enters invalid or unexpected inputs. In this example **game_board** is called using an index outside the list's of list:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   a  b  c")
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game = game_board(game, just_display=True)
game = game_board(game, 1, 3, 1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
IndexError: list index out of range
```

## 011
Best practice: use and return local/temporary variable **game_map** inside function:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   a  b  c")
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game = game_board(game, just_display=True)
game = game_board(game, 1,2,1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 1, 0]
```

## 010b
Without declaring variable as global, variable doesn't get over written:
```python
game = "I want to play a game"

def game_board():
    game = "a game"
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))
```
Prints:
```
a game
140710416855600
I want to play a game
140710383231984
```

## 010a
Global variables let us modify variables everywhere:
```python
game = "I want to play a game"

def game_board():
    global game
    game = "a game"
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))
```
Prints:
```
a game
139925773360560
a game
139925773360560
```

## 009c
Two objects of same type are **mutable**:
```python
game = [1,2,3]

def game_board():
    game[1] = 99
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))
```
Prints:
```
[1, 99, 3]
139794217624192
[1, 99, 3]
139794217624192
```

## 009b
Two objects of different type are **immutable**:
```python
game = [1,2,3]

def game_board():
    game = "a game"
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))
```
Prints:
```
a game
140350359055792
[1, 2, 3]
140350360400512
```

## 009a
Looking at the IDs we observe that function **game_board** doesn't modify variable **game**. This is called immutability:
```python
game = "I want to play a game"
print(id(game))

def game_board():
    game = "a game"
    print(id(game))
    print(game)

print(game)
game_board()
print(game)
print(id(game))
```
Prints:
```
140534510126224
I want to play a game
140534543400368
a game
I want to play a game
140534510126224
```

## 008
Function parameters, **just display** parameter to not over right player's entries:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   a  b  c")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(just_display=True)
game_board(1,2,1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 1, 0]
```

## 007d
Function parameters:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(player=0, row=0, column=0):
    print("   a  b  c")
    game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board()
game_board(1,2,1)
game_board(player=1,row=2,column=1)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 1, 0]
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 1, 0]
```

## 007c
Function parameters, default values:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board(player=0, row=0, column=0):
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)

game_board()
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
```

## 007b
Function parameters, strings:
```python
def addition(x, y):
    return x+y

z = addition("hey"," there")
print(z)
```
Prints:
```
hey there
```

## 007a
Function parameters, numbers:
```python
def addition(x, y):
    return x+y

z = addition(5,3)
print(z)
```
Prints:
```
8
```

## 006
Display game using a function:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

def game_board():
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)

game_board()
game[0][1] = 1
game_board()
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   a  b  c
0 [0, 1, 0]
1 [0, 0, 0]
2 [0, 0, 0]
```

## 005
Access each element using list's index:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
game[0][1] = 1

print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)
```
Prints:
```
   a  b  c
0 [0, 1, 0]
1 [0, 0, 0]
2 [0, 0, 0]
```

## 004
Lists:
```python
l = [1, 2, 3, 4, 5]
print(l[1])
print(l[4])
print(l[-1])
print(l[1:3])
print(l[2:])
l[2] = 99
print(l)
```
Prints:
```
2
5
5
[2, 3]
[3, 4, 5]
[1, 2, 99, 4, 5]
```

## 003b
Add row numbers using the build-in function **enumerate**:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)
```
Prints:
```
   a  b  c
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
```

## 003a
Add row numbers using a counter:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

print(" 0  1  2")
count = 0
for row in game:
    print(count, row)
    count += 1
```
Prints:
```
   0  1  2
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
```

## 002
Add column numbers:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

print(" 0  1  2")
for row in game:
    print(row)
```
Prints:
```
 0  1  2
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
```

## 001
Add list of lists and print it:
```python
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]

for row in game:
    print(row)
```
Prints:
```
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]
```

## References
- [Python built-in functions](https://docs.python.org/3/library/functions.html)