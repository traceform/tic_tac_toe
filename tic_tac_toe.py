from random import randrange

## Global variables
# WARNING: Using a string above 1 length or an integer will cause errors
CPU_SIGN = 'X'
PLAYER_SIGN = 'O'   

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

        first_valid, last_valid = board[0][0], board[-1][-1]

        # If the user input is a valid option
        if first_valid <= move <= last_valid:
            # Remove 1 from move to account for index 0
            move -= 1  # Ex.: 6 becomes 5
            # Calculate length of the matrix
            rows, columns = len(board), len(board[0])
            # Ex.: 5 // 3 equals 1, so index 1 which is row 2
            row = move // rows
            # Ex.: 5 % 3 equals 2, so index 2 which is column 3
            column = (move % columns)

            # If the selected field is in the valid moves list
            if (row, column) in VALID_MOVES:
                # replace/mark with the PLAYER_SIGN
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
                valid_moves.append((r, c))
                
    return valid_moves

def victory_for(board, sign):
    """Analyzes the board's status in order to check if a player won"""
    players = {
        CPU_SIGN: "The computer won!",
        PLAYER_SIGN: "You won!"
        }

    VALID_MOVES = make_list_of_free_fields(board)

    # Check if there are available moves
    if VALID_MOVES:
        # Check diagonal first
        if sign == board[0][0] == board[1][1] == board[2][2]:
            return players[sign]
        elif sign == board[0][2] == board[1][1] == board[2][0]:
            return players[sign]
        else:
            # Iterate through each row to look for any horizontal and vertical matches
            total_rows = len(board)
            for r in range(total_rows):
                total_hor, total_vert = 0, 0
                #print(f"Debug: R {board[r]}")

                # Iterate from column to column
                total_columns = len(board[r])
                for c in range(total_columns):
                    #print(f"Debug: R: {board[r]} | C: {c} > Total R: {total_rows} | Total C: {total_columns}")
                    # Check horizontal
                    # If the current field is equal to the chosen sign, add 1
                    match_horizontal = board[r][c] == sign
                    if match_horizontal:
                        total_hor += 1
                    
                    # Check vertical
                    # If the current field is equal to the chosen sign, add 1
                    match_vertical = board[c][r] == sign
                    if match_vertical:
                        total_vert += 1
                        
                    # If the amount of matches is equal to the length of that row/column
                    #print(f"Debug: Match H: {match_horizontal} - Total: {total_hor} | Match V: {match_vertical} - Total: {total_vert}")
                    if total_hor == total_columns or total_vert == total_rows:
                        return players[sign]
    else:
        return "Tie!"

def draw_move(board):
    """Draws the computer's move and updates the board"""
    # Picking a random number
    random_number = randrange(0, len(VALID_MOVES))
    #print(random_number)
    # Choosing the index number
    chosen = VALID_MOVES[random_number]
    # Marking the chosen field
    board[chosen[0]][chosen[1]] = CPU_SIGN
    
    return board, CPU_SIGN

if __name__ == "__main__":
    # Creates the board
    board = [[n for n in range(1, 3+1)], [n for n in range(4, 6+1)], [n for n in range(7, 9+1)]]

    VALID_MOVES = make_list_of_free_fields(board)
    play = 1
    while play:
        if play % 2 != 0:
            # Robot's turn
            board, sign = draw_move(board)
        else:
            # Player's turn
            try:
                board, sign = enter_move("Enter your move: ", board)
            except KeyboardInterrupt:
                print("\nProgram terminated.")
                exit()

        play += 1
            
        display_board(board)
        message = victory_for(board, sign)
        if message:
            print(message)
            quit()
