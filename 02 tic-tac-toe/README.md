# tic tac toe game

## 013d
Diagonal winner:

## 013c
Vertical winner:

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
This works but it's hardcoded. The right way to do it is doing it dynamically (and with less code) so the same code works for different board sizes. In the following example we will use the built-in functions `count` to count the number of appareances of the row's first element and compare it against the length of the row using `len`:
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
