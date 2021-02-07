"""git repo link: https://github.com/vsaliievaa/Skyscrapers-Game"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    """
    lines = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible
    looking to the right, False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    >>> left_to_right_check("132354*", 3)
    False
    """
    visible = 0
    input_line = input_line[1:-1]
    first = input_line[0]
    for i in range(1, len(input_line)):
        if input_line[i] > first:
            first = input_line[i]
            visible += 1
    if visible == pivot - 1:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
        '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(len(board)):
        if '?' in board[i]:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
        '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    lst = []
    for i in range(len(board)):
        lst = []
        row = board[i][1:-1]
        for k in range(len(row)):
            if str(row[k]) not in lst or row[k] == '*':
                lst.append(str(row[k]))
            else:
                return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    left_prompts, right_prompts = [], []
    reverse = []

    for i in range(1, len(board) - 1):
        left_prompts.append(board[i][0])
        right_prompts.append(board[i][-1])
    board = board[1:-1]
    for i in range(len(board)):
        if left_prompts[i] != '*':
            if not left_to_right_check(input_line=board[i], pivot=int(left_prompts[i])):
                return False
    for i in range(len(board)):
        reverse.append(board[i][::-1])
    for i in range(len(reverse)):
        if right_prompts[i] != '*':
            if not left_to_right_check(input_line=reverse[i], pivot=int(right_prompts[i])):
                return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for rows, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
        '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
        '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
        '*35214*', '*41532*', '*2*1***'])
    False
    """
    columns = []
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        columns.append(''.join(col))
    columns = columns[::-1]
    uniqueness = check_uniqueness_in_rows(columns)
    visibility = check_horizontal_visibility(columns)
    if uniqueness and visibility:
        return True
    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    """
    board = read_input(input_path)
    if check_uniqueness_in_rows(board) and check_not_finished_board(board):
        is_winning = check_horizontal_visibility(
            board) and check_columns(board)
    return is_winning
