from ..utils import has_method

class BaseAgent():
  def add_to_game(self, game):
    self.game = game
    self.board = game.board
    if has_method(self, 'post_add_to_game'):
      self.post_add_to_game()

  def place_block(self):
    raise NotImplementedError('place_block must be implemented')