def play():
    # Initialize the game board (empty 3x3 grid)
    board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    
    def display_board(board):
        print("\n Current board:")
        for row in board:
            print(" | ".join(row))
            print("-" * 9)
    
    def check_win(board, player):
        # Check rows
        for row in board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def check_tie(board):
        return all(cell != " " for row in board for cell in row)
    
    def player_input(player):
        while True:
            try:
                row = int(input(f"Player {player}, enter row (1-3): ")) - 1
                col = int(input(f"Player {player}, enter column (1-3): ")) - 1
                if row not in range(3) or col not in range(3):
                    print("Invalid input. Rows and columns must be 1, 2, or 3.")
                elif board[row][col] != " ":
                    print("That cell is already occupied. Try again.")
                else:
                    return row, col
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    current_player = "X"
    
    while True:
        display_board(board)
        row, col = player_input(current_player)
        board[row][col] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
play()

