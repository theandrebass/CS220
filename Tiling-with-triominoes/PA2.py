def triominoes(n, removed_row=0, removed_column=0):
    """
    # tile a chessboard of size 2^n x 2^n with L-shaped triominoes with a
    # missing square whose position is given by (removed_row, removed_column)
    # return value:
    # the return value is a list of lists, where element i,j is associated with
    # position i,j in the board; each square is assigned an integer value which
    # is the identifier of the triomino in that position.
    # for example, a possible return value for n = 1 is:
    # [ [1, 1], [1, 2] ]
    # the value 1 corresponds to the squares covered by the triomino, and the
    # value 2 corresponds to the removed square.
    # an example for n = 2:
    # [ [1,1,2,2],[1,3,3,2],[4,3,5,5],[4,4,5,6] ]
    # This includes entries for triominoes with IDs 1,...,5 and 6 is the value
    # associated with the removed square.
    # There are no constraints on how you should number the triominoes/removed
    # square.
    # arguments:
    # n:  the parameter for the size of the board
    # removed_row, removed_column:  the row and column in the matrix where the removed
    # square should be placed, i.e.
    # board[removed_row][removed_column] should contain the unique value associated
    # with the removed square
    """

    colors = range(1, (2 ** (2 * n)) / 3 + 1)

    return triomino_helper(n, [removed_row, removed_column], colors)


def triomino_helper(n, position, next_color_list) :

    if n == 1:
        next_color = next_color_list.pop()
        if position == [0, 0] :
            return [[0, next_color], [next_color, next_color]]
        elif position == [1, 0] :
            return [[next_color, next_color], [0, next_color]]
        elif position == [0, 1] :
            return [[next_color, 0], [next_color, next_color]]
        elif position == [1, 1] :
            return [[next_color, next_color], [next_color, 0]]

    if position[0] >= 2**(n - 1) :
        if position[1] >= 2**(n - 1) : # bottom right
            board0 = triomino_helper(n - 1, [2**(n - 1) - 1, 0], next_color_list)
            board1 = triomino_helper(n - 1, [2**(n - 1) - 1, 2**(n - 1) - 1], next_color_list)
            board2 = triomino_helper(n - 1, [0, 2**(n - 1) - 1], next_color_list)
            board3 = triomino_helper(n - 1, [position[0] - 2**(n - 1), position[1] - 2**(n - 1)], next_color_list)
            next_color = next_color_list.pop()
            board0[2**(n - 1) - 1][0] = next_color
            board1[2**(n - 1) - 1][2**(n - 1) - 1] = next_color
            board2[0][2**(n - 1) - 1] = next_color
            return quadrant_combine(board0, board1, board2, board3)
        else : # bottom left
            board0 = triomino_helper(n - 1, [2 ** (n - 1) - 1, 0], next_color_list)
            board1 = triomino_helper(n - 1, [2 ** (n - 1) - 1, 2 ** (n - 1) - 1], next_color_list)
            board2 = triomino_helper(n - 1, [position[0] - 2**(n - 1), position[1]], next_color_list)
            board3 = triomino_helper(n - 1, [0, 0], next_color_list)
            next_color = next_color_list.pop()
            board0[2 ** (n - 1) - 1][0] = next_color
            board1[2 ** (n - 1) - 1][2 ** (n - 1) - 1] = next_color
            board3[0][0] = next_color
            return quadrant_combine(board0, board1, board2, board3)
    else :
        if position[1] >= 2**(n - 1) : # top right
            board0 = triomino_helper(n - 1, [position[0], position[1] - 2**(n - 1)], next_color_list)
            board1 = triomino_helper(n - 1, [2 ** (n - 1) - 1, 2 ** (n - 1) - 1], next_color_list)
            board2 = triomino_helper(n - 1, [0, 2**(n - 1) - 1], next_color_list)
            board3 = triomino_helper(n - 1, [0, 0], next_color_list)
            next_color = next_color_list.pop()
            board1[2 ** (n - 1) - 1][2 ** (n - 1) - 1] = next_color
            board2[0][2 ** (n - 1) - 1] = next_color
            board3[0][0] = next_color
            return quadrant_combine(board0, board1, board2, board3)
        else : # top left
            board0 = triomino_helper(n - 1, [2 ** (n - 1) - 1, 0], next_color_list)
            board1 = triomino_helper(n - 1, [position[0], position[1]], next_color_list)
            board2 = triomino_helper(n - 1, [0, 2 ** (n - 1) - 1], next_color_list)
            board3 = triomino_helper(n - 1, [0, 0], next_color_list)
            next_color = next_color_list.pop()
            board0[2 ** (n - 1) - 1][0] = next_color
            board2[0][2 ** (n - 1) - 1] = next_color
            board3[0][0] = next_color
            return quadrant_combine(board0, board1, board2, board3)

def quadrant_combine(board0, board1, board2, board3) :
    board = []
    for i in range(len(board1)) :
        row = []
        row.extend(board1[i])
        row.extend(board0[i])
        board.append(row)
    for i in range(len(board3)) :
        row = []
        row.extend(board2[i])
        row.extend(board3[i])
        board.append(row)
    return board
