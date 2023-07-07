import pdb

class Board:
  def __init__(self, column_count=7, row_count=6):
    self.column_count = column_count
    self.row_count = row_count
    self.create_grid()

  def create_grid(self):
    gridline = []
    for _ in range(self.column_count):
        gridline.append('-')
    grid = []
    for _ in range(self.row_count):
        grid.append(list(gridline))

    print(f'grid has {len(grid)} rows and {len(grid[0])} columns')
    self.grid = grid
  
  def print_board(self):
    for i in range(self.row_count):
      print(self.grid[i])
    print([f'{i}' for i in range(self.column_count)])

  def place_block(self, column, symbol):
    print(f'placing column {column} with symbol {symbol}')
    row = False
    row = self.find_next_free_row(column)
    self.grid[row][column] = symbol
    return {
      'row': row,
      'column': column,
    }
  
  def validate_move(self, column):
    if column < 0 or column > self.column_count - 1:
      return False
    row = self.find_next_free_row(column)
    if row < 0 or row > self.row_count:
      return False
    return True
  
  def find_next_free_row(self, column):
    row = -1
    for i in reversed(range(self.row_count)):
      if self.grid[i][column] == '-':
        print(f'found free row {i}')
        row = i
        break

    return row
  
  def get_row(self, row):
    return self.grid[row]

  def get_column(self, column):
    return [row[column] for row in self.grid]

  def get_cell(self, row, column):
    print(f'getting cell at row {row} and column {column}')
    # pdb.set_trace()
    return self.grid[row][column]