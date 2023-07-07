class BaseAgent():
  def add_to_game(self, game):
    self.game = game
    self.board = game.board

  def place_block(self):
    raise NotImplementedError('place_block must be implemented')