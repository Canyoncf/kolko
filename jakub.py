var = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0
w = 0
def display_board():
    print('+', '+', '+', '+', sep="-------")
    print('|', '|', '|', '|', sep="       ")
    print('|',var[0] , '|',var[1], '|',var[2], '|', sep="   ")
    print('|', '|', '|', '|', sep="       ")
    print('+', '+', '+', '+', sep="-------")
    print('|', '|', '|', '|', sep="       ")
    print('|',var[3] , '|',var[4], '|',var[5], '|', sep="   ")
    print('|', '|', '|', '|', sep="       ")
    print('+', '+', '+', '+', sep="-------")
    print('|', '|', '|', '|', sep="       ")
    print('|',var[6] , '|',var[7], '|',var[8], '|', sep="   ")
    print('|', '|', '|', '|', sep="       ")
    print('+', '+', '+', '+', sep="-------")

def zank(z):
    z = z%2
    point = ["O", "X"]
    znak = point[z]
    print(z)
    return znak

def enter_move(znak,n):
    x = int(input("Podaj miejsce :"))
    #sprawdzenie
    for i in range(len(var)):
        if int(i+1) == x:
            var[i] = znak
            n += 1
            display_board()



    # checks the input, and updates the board according to t
    #     # The function accepts the board's current status, asks the user about their move,he user's decision.


def make_list_of_free_fields():
    while 11 in var2:
        var2.remove(11)
    while 99 in var2:
        var2.remove(99)
    print(var2)

    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(znak):
    if (var[0] == var[1] == var[3]) or (var[3] == var[4] == var[5]) or (var[6] == var[7] == var[8]) or (var[0] == var[3] == var[6]) or (
        var[1] == var[4] == var[7]) or (var[2] == var[5] == var[8]) or (var[0] == var[1] == var[2]) or (var[3] == var[4] == var[5]) or (
        var[0] == var[4] == var[8]) or (var[2] == var[4] == var[6] ):
        print("wygrał ten znak:",znak)
        w = 1
        return w





    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.


if not w == 1:
    n = 0
    z = 0
    display_board()
    while w == 0:
        z = z + 1
        znak = zank(z)
        enter_move(znak,n)
        victory_for(znak)
else:
    breakpoint()
