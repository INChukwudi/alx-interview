#!/usr/bin/python3

"""
python module that executes to solve the nqueens problem
"""

import sys


def is_spot_safe(board, row, col, N):
    """
    Function that checks if it is safe to place a queen
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def perform_placement(board, col, N):
    """
    Function that performs the placement of queens on the
    n x n chess board
    """
    if col >= N:
        solution = []
        for row in range(N):
            for c in range(N):
                if board[row][c] == 1:
                    solution.append([row, c])
        print(solution)
        return True

    result = False
    for i in range(N):
        if is_spot_safe(board, i, col, N):
            board[i][col] = 1
            result = perform_placement(board, col + 1, N) or result
            board[i][col] = 0

    return result


def main():
    """
    Function that controls the flow of execution of the script
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    perform_placement(board, 0, N)


if __name__ == "__main__":
    main()
