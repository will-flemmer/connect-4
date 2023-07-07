from . import Board

def test_print_board():
  board = Board()
  board.print_board()
  assert True

def test_can_return_a_column():
  board = Board()
  board.grid[0][0] = 'R'
  board.grid[1][0] = 'R'
  board.grid[2][0] = 'R'
  board.grid[3][0] = 'R'
  assert board.get_column(0) == ['R', 'R', 'R', 'R', '-', '-']

def test_can_return_a_row():
  board = Board()
  board.grid[0][0] = 'R'
  board.grid[0][1] = 'R'
  board.grid[0][2] = 'R'
  board.grid[0][3] = 'R'
  assert board.get_row(0) == ['R', 'R', 'R', 'R', '-', '-', '-']

def test_can_get_cell():
  board = Board()
  board.grid[0][0] = 'R'
  assert board.get_cell(0, 0) == 'R'
  assert board.get_cell(1, 0) == '-'