
class BoardEvaluator():
  def __init__(self, board, red_agent, blue_agent):
    self.board = board
    self.winner = None
    self.max_row = board.row_count - 1
    self.max_column = board.column_count - 1

  def evaluate(self, agent, coords):
    self.board.print_board()
    if not agent or not coords:
      raise Exception(
        f'Invalid evaluation, missing agent or coords - agent: {agent}, coords: {coords}'
      )
    self.current_agent = agent
    self.current_coords = coords
    self.current_symbol = agent.symbol
    self.check_for_horizontal_win()
    self.check_for_vertical_win()
    self.check_for_diagonal_win()
    self.is_draw()

    return {
      'completed': self.is_completed(),
      'winner': self.winner,
    }

  def check_for_horizontal_win(self):
    if self.winner or self.is_draw():
      return
    row = self.board.get_row(self.current_coords["row"])
    self.check_array_for_win(row)

  def check_array_for_win(self, array):
    current_count = 0
    for i in array:
      if current_count == 4:
        break
      if i == self.current_symbol:
        current_count += 1
      else:
        current_count = 0
    if current_count == 4:
      self.winner = self.current_agent

  def check_for_vertical_win(self):
    if self.winner or self.is_draw():
      return
    column = self.board.get_column(self.current_coords["column"])
    self.check_array_for_win(column)
  
  def check_for_diagonal_win(self):
    if self.winner or self.is_draw():
      return
    positive_diagonal = self.create_positive_diagonal_array(self.current_coords["row"], self.current_coords["column"])
    negative_diagonal = self.create_negative_diagonal_array(self.current_coords["row"], self.current_coords["column"])
    self.check_array_for_win(positive_diagonal)
    self.check_array_for_win(negative_diagonal)

  def create_positive_diagonal_array(self, row, column):
    diagonal = []
    while row > 0 and column > 0:
      row -= 1
      column -= 1
    
    while row < (self.max_row) and column < (self.max_column):
      diagonal.append(self.board.get_cell(row, column))
      row += 1
      column += 1
    return diagonal

  def create_negative_diagonal_array(self, row, column):
    diagonal = []
    min_row = row
    max_column = column
    while min_row > 0 and max_column < (self.max_column):
      min_row -= 1
      max_column += 1
    
    while min_row < (self.max_row) and max_column >= 0:
      diagonal.append(self.board.get_cell(min_row, max_column))
      min_row += 1
      max_column -= 1
    return diagonal

  def is_completed(self):
    return self.is_draw() or bool(self.winner)

  def is_draw(self):
    return False