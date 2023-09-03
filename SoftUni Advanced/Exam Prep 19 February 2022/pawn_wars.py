def check_white_win(r, c, size):
    if 0 <= c - 1 < size:
        if board[r - 1][c - 1] == "b":
            return r - 1, c - 1
    if 0 <= c + 1 < size:
        if board[r - 1][c + 1] == "b":
            return r - 1, c + 1


def check_black_win(r, c, size):
    if 0 <= c - 1 < size:
        if board[r + 1][c - 1] == "w":
            return r + 1, c - 1
    if 0 <= c + 1 < size:
        if board[r + 1][c + 1] == "w":
            return r + 1, c + 1


size = 8

board = []

positions = {

    "w": [],
    "b": []

}

for row in range(size):
    board.append(input().split())
    for col in range(size):
        if board[row][col] == "w":
            positions["w"] = [row, col]
        elif board[row][col] == "b":
            positions["b"] = [row, col]

winning_pos = []
white_promoted = False
black_promoted = False
white_win = False
black_win = False

for _ in range(1, 14):

        if _ % 2 != 0:

            if check_white_win(positions["w"][0], positions["w"][1], size):
                win_row, win_col = check_white_win(positions["w"][0], positions["w"][1], size)
                winning_pos.append(win_row)
                winning_pos.append(win_col)
                white_win = True
                break

            board[positions["w"][0]][positions["w"][1]] = "-"
            positions["w"][0] -= 1

            board[positions["w"][0]][positions["w"][1]] = "w"

            if positions["w"][0] == 0:
                winning_pos.append(positions["w"][0])
                winning_pos.append(positions["w"][1])
                white_promoted = True
                break

        if _ % 2 == 0:
            if check_black_win(positions["b"][0], positions["b"][1], size):
                win_row, win_col = check_black_win(positions["b"][0], positions["b"][1], size)
                winning_pos.append(win_row)
                winning_pos.append(win_col)
                black_win = True
                break

            board[positions["b"][0]][positions["b"][1]] = "-"
            positions["b"][0] += 1

            board[positions["b"][0]][positions["b"][1]] = "b"
            if positions["b"][0] == 7:
                winning_pos.append(positions["b"][0])
                winning_pos.append(positions["b"][1])
                black_promoted = True
                break


if white_promoted:
    print(f"Game over! White pawn is promoted to a queen at {chr(97 + winning_pos[1])}{8 -winning_pos[0]}.")
if black_promoted:
    print(f"Game over! Black pawn is promoted to a queen at {chr(97 + winning_pos[1])}{8 - winning_pos[0]}.")
if white_win:
    print(f"Game over! White win, capture on {chr(97 + winning_pos[1])}{8 - winning_pos[0]}.")
if black_win:
    print(f"Game over! Black win, capture on {chr(97 + winning_pos[1])}{8 - winning_pos[0]}.")
