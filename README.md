# Skyscrapers-Game
This module allows the user to play a skyscrapers game. The Skyscrapers Game is a logic game. The goal is to place skyscrapers of different height all over the game board, complying to a set of rules:
1) A skyscraper is called visible from a position if a previous one is lower or of the same height (height are natural numbers, e.g. 1, 2, 3 etc.) The number of visible skyscrapers in every column and row must match a hint (a hint is a left-most and right-most number in every row and column. "*" means that the hint is absent).
2) Every skyscraper in a row must have unique height.
3) Every skyscraper in a column must have unique height.
The state of the game board comes as a .txt file, all functions, except read_input(), return boolean values.
The module consists of the main function, check_skyscrapers(), and six smaller functions. check_skyscrapers() takes the game board as a list of lists, checks its status, and returns boolean value, defining whether this state of game board is winning (True) or not (False).
read_input() takes a path to a file with the state of game board as game string and returns list of lists.
left_to_right_check() takes in input-line - a row of game board as a string, and pivot - number on the left-most hint of the input_line. It returns True if number of buildings from the left-most hint is visible from the left to the right, and False otherwise.
check_not_finished_board() returns False, if game board is not complete (if at least one '?' is present in the taken list of lists), and True otherwise.
check_uniqueness_in_rows() takes a list of lists and checks its uniqueness. If height of every building in a row is unique, returns True, otherwise - returns False.
check_horizontal_visibility() takes in a list of lists and checks if all the hints are satisfied, looking from the left to the right and vice-versa. Returns True if all criterias are fulfilled and False otherwise.
check_columns() is a combination of check_horizontal_visibility() and check_uniqueness_in_rows(), but for columns. Returns True if all criterias are fulfilled and False otherwise.
 
