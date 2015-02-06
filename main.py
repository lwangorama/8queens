
# successful result list
results = []


def create_board():
    # create a 8x8 matrix lists initialized to 0
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return board


def is_conflict(board, row, col):
    # occupied?
    if board[row][col] > 0:
        return True

    # horizontal conflict?
    for i in range(8):
        if board[row][i] > 0:
            return True

    # vertical conflict?
    for i in range(8):
        if board[i][col] > 0:
            return True

    # diagonal conflict?
    for i in range(8):
        if row - i >= 0 and col - i >= 0:
            if board[row-i][col-i] > 0:
                return True
        if row + i < 8 and col + i < 8:
            if board[row+i][col+i] > 0:
                return True
        if row - i >= 0 and col + i < 8:
            if board[row-i][col+i] > 0:
                return True
        if row + i < 8 and col - i > 0:
            if board[row+i][col-i] > 0:
                return True

    # no conflict
    return False


def find_possible_col(queen_list):
    board = create_board()
    for pos in queen_list:
        board[pos[0]][pos[1]] = 1
    row = queen_list[-1][0] + 1 if queen_list else 0

    positions = []
    for col in range(8):
        if not is_conflict(board, row, col):
            positions.append(col)
    return positions


def find_answer(queen_list):
    row = queen_list[-1][0] if queen_list else -1

    cols = find_possible_col(queen_list)
    if not cols:
        return queen_list
    if len(queen_list) + 1 == 8:
        queen_list.append((row + 1, cols[0]))
        results.append(queen_list)
        return queen_list

    for col in cols:
        new_list = queen_list.copy()
        new_list.append((row + 1, col))
        find_answer(new_list)


def main():
    find_answer([])
    for result in results:
        print(result)
    print()
    print("{0} solutions found".format(len(results)))


if __name__ == "__main__":
    main()
