from tic_tac_toe import victory_for

# Global variables
PLAYER_SIGN = 'O'
CPU_SIGN = 'X'

PLAYER_WON = "You won!"
CPU_WON = "The computer won!"
TIE = "Tie!"

def print_msg(prompt, msg):
    if msg == PLAYER_WON:
        print(prompt + msg)
    elif msg == CPU_WON:
        print(prompt + msg)
    else:
        print(f"Unexpected: {msg}")

def test_victory_for(sign):
    _ = sign

    board = [
        [ _ , _ , _ ],
        [ 4 , 5 , 6 ],
        [ 7 , 8 , 9 ]
    ]

    msg = victory_for(board, _)
    print_msg("Row 1 test successful: ", msg)

    board = [
        [ 1 , 2 , 3 ],
        [ _ , _ , _ ],
        [ 7 , 8 , 9 ]
    ]
    msg = victory_for(board, _)
    print_msg("Row 2 test successful: ", msg)

    board = [
        [ 1 , 2 , 3 ],
        [ 4 , 5 , 6 ],
        [ _ , _ , _ ]
    ]
    msg = victory_for(board, _)
    print_msg("Row 3 test successful: ", msg)

    board = [
        [ _ , 2 , 3 ],
        [ _ , 5 , 6 ],
        [ _ , 8 , 9 ]
    ]
    msg = victory_for(board, _)
    print_msg("Column 1 test successful: ", msg)

    board = [
        [ 1 , _ , 3 ],
        [ 4 , _ , 6 ],
        [ 7 , _ , 9 ]
    ]
    msg = victory_for(board, _)
    print_msg("Column 2 test successful: ", msg)

    board = [
        [ 1 , 2 , _ ],
        [ 4 , 5 , _ ],
        [ 7 , 8 , _ ]
    ]
    msg = victory_for(board, _)
    print_msg("Column 3 test successful: ", msg)

    board = [
        [ _ , 2 , 3 ],
        [ 4 , _ , 6 ],
        [ 7 , 8 , _ ]
    ]
    msg = victory_for(board, _)
    print_msg("Diagonal test 1 successful: ", msg)

    board = [
        [ 1 , 2 , _ ],
        [ 4 , _ , 6 ],
        [ _ , 8 , 9 ]
    ]
    msg = victory_for(board, _)
    print_msg("Diagonal test 1 successful: ", msg)

    board = [
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_']
    ]
    msg = victory_for(board, _)
    print_msg("Tie test successful: ", msg)

# Test player
test_victory_for(PLAYER_SIGN)
# Test CPU
#test_victory_for(CPU_SIGN)
