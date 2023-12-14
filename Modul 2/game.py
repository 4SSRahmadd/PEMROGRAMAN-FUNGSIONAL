import random

def create_board(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_board(board):
    for row in board:
        print(' - '.join(row))

def generate_pawn_position(board):
    empty_cells = [(row, col) for row in range(len(board))
                   for col in range(len(board[0])) if board[row][col] == ' ']
    if not empty_cells:
        raise Exception("No empty cells available.")
    return random.choice(empty_cells)
    
def is_game_won(board, goal_pos): return board[goal_pos[0]][goal_pos[1]] == 'A'

def is_out_of_bounds(board, row, col):
    return row < 0 or row >= len(board) or col < 0 or col >= len(board[0])


def play_game():
    while True:
        width = int(input("Enter the width of the board: "))
        height = int(input("Enter the height of the board: "))

        initial_board = create_board(width, height)

        pawn_pos = generate_pawn_position(initial_board)

        goal_pos = generate_pawn_position(initial_board)

        initial_board[pawn_pos[0]][pawn_pos[1]] = 'A'
        initial_board[goal_pos[0]][goal_pos[1]] = 'O'

        print("Initial board:")
        print_board(initial_board)

        generate_new_positions_count = 0
        while generate_new_positions_count < 3:
            generate_new_positions = input(
                "Do you want to generate new positions for the pawn and goal? (Y/N): ")

            if generate_new_positions.upper() == 'Y':
                current_board = create_board(
                    width, height)
                pawn_pos = generate_pawn_position(current_board) 

                goal_pos = generate_pawn_position(current_board)
                current_board[pawn_pos[0]][pawn_pos[1]] = 'A'
                current_board[goal_pos[0]][goal_pos[1]] = 'O'
                generate_new_positions_count += 1
                print("New positions generated.")
                print("Updated board:")
                print_board(current_board)
            else:
                current_board = initial_board
                break

        print("Let's start the game!")

        moves = input("Enter your move sequence (WASD): ")

        for move in moves:
            row, col = pawn_pos
            if move == 'W':
                row -= 1
            elif move == 'A':
                col -= 1
            elif move == 'S':
                row += 1
            elif move == 'D':
                col += 1

            if is_out_of_bounds(current_board, row, col):
                print("Out of bounds")
                break

            if move == 'W' and pawn_pos[0] > 0:
                current_board[pawn_pos[0]][pawn_pos[1]
                                           ], current_board[pawn_pos[0] - 1][pawn_pos[1]] = ' ', 'A'
                pawn_pos = (pawn_pos[0] - 1, pawn_pos[1])
            elif move == 'A' and pawn_pos[1] > 0:
                current_board[pawn_pos[0]][pawn_pos[1]
                                           ], current_board[pawn_pos[0]][pawn_pos[1] - 1] = ' ', 'A'
                pawn_pos = (pawn_pos[0], pawn_pos[1] - 1)
            elif move == 'S' and pawn_pos[0] < height - 1:
                current_board[pawn_pos[0]][pawn_pos[1]
                                           ], current_board[pawn_pos[0] + 1][pawn_pos[1]] = ' ', 'A'
                pawn_pos = (pawn_pos[0] + 1, pawn_pos[1])
            elif move == 'D' and pawn_pos[1] < width - 1:
                current_board[pawn_pos[0]][pawn_pos[1]
                                           ], current_board[pawn_pos[0]][pawn_pos[1] + 1] = ' ', 'A'
                pawn_pos = (pawn_pos[0], pawn_pos[1] + 1)
            else:
                print("Invalid move. Please use WASD keys.")
                break

            if is_game_won(current_board, goal_pos):
                print("Current board:")
                print_board(current_board)
                print("You Win!")
                break
        else:
            print("Current board:")
            print_board(current_board)
            print("You Lose!")

        play_again = input("Wanna try again? (Y/N): ")
        if play_again.upper() != 'Y':
            print("See you again...")
            break


if __name__ == "__main__":
    play_game()
