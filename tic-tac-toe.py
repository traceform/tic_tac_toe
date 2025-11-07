from random import randrange

def display_board(board):
    """Prints the formatted board status to the console"""
    # Setting a dictionary to aid in the formatting
    f = {
    1: board[0][0],
    2: board[0][1],
    3: board[0][2],
    4: board[1][0],
    5: board[1][1],
    6: board[1][2],
    7: board[2][0],
    8: board[2][1],
    9: board[2][2]
    }

    print(f"""\
+-------+-------+-------+
|       |       |       |
|   {f[1]}   |   {f[2]}   |   {f[3]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {f[4]}   |   {f[5]}   |   {f[6]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {f[7]}   |   {f[8]}   |   {f[9]}   |
|       |       |       |
+-------+-------+-------+\
    """)

def enter_valid_move():
    while True:
        try:
            move = int(input("Invalid number! Try again: "))
            return move
        except ValueError:
            pass

def enter_move(prompt, board):
    """Prompts the user for an integer, then validates the input and makes the move"""
    
    while True:
        try:
            move = int(input(prompt))
        except ValueError:
            move = enter_valid_move()

        # If the user input is a valid option
        if FIRST_VALID <= move <= LAST_VALID:
            # Remove 1 from move to account for index 0
            move -= 1  # Ex.: 6 becomes 5
            # Calculate length of the matrix
            rows, columns = len(board), len(board[0])
            # Ex.: 5 // 3 equals 1, so index 1 which is row 2
            row = move // rows
            # Ex.: 5 % 3 equals 2, so index 2 which is column 3
            column = (move % columns)

            if isinstance(board[row][column], int):
                # If the field's value is still an integer, replace/mark with 'O'
                board[row][column] = PLAYER_SIGN
                return board, PLAYER_SIGN
            else:
                print("This field is already occupied. Try again! ", end='')
        else:
            print("Your move must be greater than 0 and less than 10. ", end='')

def make_list_of_free_fields(board):
    """Browses the board and builds a list of all the free squares"""
    valid_moves = []
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if isinstance(board[r][c], int):
                valid_moves.append((r,c))
                
    return valid_moves

def victory_for(board, sign):
    """Analyzes the board's status in order to check if a player won"""
    players = {
        'X': "The computer won!",
        'O': "You won!"
        }

    msg = None
    '''
    # Check horizontal
    if board[0][0] == board[0][1] == board[0][2]: # 1-3
    if board[1][0] == board[1][1] == board[1][2]: # 4-6
    if board[2][0] == board[2][1] == board[2][2]: # 7-9
    # Check vertical
    if board[0][0] == board[1][0] == board[2][0]: # 1,4,7
    if board[0][1] == board[1][1] == board[2][1]: # 2,5,8
    if board[0][2] == board[1][2] == board[2][2]: # 3,6,9
    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2]: # 1,5,9
    if board[2][0] == board[1][1] == board[0][2]: # 7,5,3

    # Iterate through each row
    for row in board:
        print(row)
        # Iterate from column to column
        for column in row:
            print(column)
            # Compare every field with the sign
            equal = column == sign
            # If the current field is different, stop
            if not equal:
                break
        # If equal was never False, return the winning message
        if equal:
                return players[sign]
    '''

    # Check if there are available moves
    if VALID_MOVES:
        # Check diagonal first
        if board[0][0] == sign:
            if board[1][1] == sign:
                if board[2][2] == sign:
                    return players[sign]
        elif board[2][0] == sign:
            if board[1][1] == sign:
                if board[0][2] == sign:
                    return players[sign]
        else:
            # Iterate through each row
            for i in range(len(board)):
                #print('i',board[i])
                # Iterate from column to column
                total_horizontal, total_vertical = 0, 0
                
                for j in range(len(board[i])):
                    # If the current field is equal, count 1
                    match_horizontal = board[i][j] == sign
                    if match_horizontal:
                        total_horizontal += 1

                    match_vertical = board[j][i] == sign
                    if match_vertical:
                        total_vertical += 1
                        
                    # If equal was never False, return the winning message
                    if total_horizontal == len(board[i]) or total_vertical == len(board):
                        return players[sign]
            return msg
    else:
        return "Tie!"

def draw_move(board):
    """Draws the computer's move and updates the board"""

    # Checking valid moves
    valid_moves = make_list_of_free_fields(board)
    #print(valid_moves)
    # Picking up a random number
    random_number = randrange(0,len(valid_moves))
    #print(random_number)
    # Choosing the index number
    chosen = valid_moves[random_number]
    # Marking the chosen field
    board[chosen[0]][chosen[1]] = CPU_SIGN
    
    return board, CPU_SIGN

if __name__ == "__main__":
    # Global variables
    CPU_SIGN = 'X'
    PLAYER_SIGN = 'O'
    
    # Creates the board
    board = [[n for n in range(1, 3+1)], [n for n in range(4, 6+1)], [n for n in range(7, 9+1)]]

    # Collects the first and last valid options for later use
    FIRST_VALID, LAST_VALID = board[0][0], board[-1][-1]

    play = 1
    while play:
        if play % 2 != 0:
            # Robot's turn
            board, sign = draw_move(board)
        else:
            # Player's turn
            board, sign = enter_move("Enter your move: ", board)

        play += 1
            
        display_board(board)
        VALID_MOVES = make_list_of_free_fields(board)
        message = victory_for(board, sign)
        if message:
            print(message)
            quit()
