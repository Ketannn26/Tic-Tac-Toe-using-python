import random

def print_board(board):
  """Prints the Tic Tac Toe board."""
  for row in board:
    print(" | ".join(row))
    print("-" * 9)

def check_win(board, player):
  """Checks if a player has won the game."""
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True
  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  # Check diagonals
  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
    return True
  return False

def is_board_full(board):
  """Checks if the board is full."""
  return all(all(cell != " " for cell in row) for row in board)

def get_player_move(board):
  """Gets the player's move."""
  while True:
    try:
      move = int(input("Enter your move (1-9): "))
      if 1 <= move <= 9 and board[(move - 1) // 3][(move - 1) % 3] == " ":
        return move - 1
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_computer_move(board):
  """Gets the computer's move."""
  # Check for winning move
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        if check_win(board, "O"):
          board[i][j] = " "
          return i * 3 + j + 1
        board[i][j] = " "
  # Check for blocking move
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "X"
        if check_win(board, "X"):
          board[i][j] = " "
          return i * 3 + j + 1
        board[i][j] = " "
  # Choose a random empty cell
  empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
  i, j = random.choice(empty_cells)
  return i * 3 + j + 1

def play_game():
  """Plays a Tic Tac Toe game."""
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"
  while True:
    print_board(board)
    if current_player == "X":
      move = get_player_move(board)
    else:
      move = get_computer_move(board)
    row, col = move // 3, move % 3
    board[row][col] = current_player
    if check_win(board, current_player):
      print_board(board)
      print(f"{current_player} wins!")
      break
    if is_board_full(board):
      print_board(board)
      print("It's a tie!")
      break
    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()