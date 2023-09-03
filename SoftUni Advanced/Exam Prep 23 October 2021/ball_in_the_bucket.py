def bucket_column(r, c, matrix):
    return sum(int(r[c]) for r in matrix if r[c].isdigit())


def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True


size = 6

matrix = []
bucket_pos = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "B":
            bucket_pos.append((row, col))

total_points = 0
buckets_hit = []

for throw in range(3):

    coords = eval(input())
    row, col = coords[0], coords[1]

    if not is_valid(row, col, size):
        continue

    if matrix[row][col] == "B":
        if coords not in buckets_hit:
            buckets_hit.append((row, col))
            total_points += bucket_column(row, col, matrix)

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")

else:
    if 100 <= total_points <= 199:
        print(f"Good job! You scored {total_points} points, and you've won Football.")
    elif 200 <= total_points <= 299:
        print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
    elif total_points >= 300:
        print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
