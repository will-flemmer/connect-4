from app.agent.agent import Agent
from app.board.board import Board
from app.board_evaluator.board_evaluator import BoardEvaluator
from ..utils import has_method
import os

class LifeCycleManager():
  game_finished = False
  winner = None
  def __init__(self, red_agent, blue_agent, row_count=6, column_count=7):
    self.board = Board(row_count=row_count, column_count=column_count)
    self.grid = self.board.grid
    self.red_agent = red_agent
    self.current_turn = self.red_agent
    self.blue_agent = blue_agent
    self.red_agent.add_to_game(self)
    self.blue_agent.add_to_game(self)

  def start_game(self):
    self.evaluator = BoardEvaluator(
      self.board, self.red_agent, self.blue_agent
    )
    self.board.print_board()
    self.main_game_loop()

  def main_game_loop(self):
    while not self.game_finished:
      coords = self.make_move()
      self.evaluate_board(coords)
      self.post_evaluation_hook()

  def evaluate_board(self, coords):
    result = self.evaluator.evaluate(self.current_turn, coords)
    if result['completed']:
      self.board.print_board()
      print('Game over!')
      print(f'{result["winner"].name} has won the game!')
      self.game_finished = True
      self.winner = result['winner']
    else:
      self.current_turn = self.blue_agent if self.current_turn == self.red_agent else self.red_agent

  def make_move(self):
    os.system('clear')
    agent = self.current_turn
    self.board.print_board()
    print(f'{agent.name}\'s turn ({agent.color})')
    return agent.place_block()

  def post_evaluation_hook(self):
    if has_method(self.red_agent, 'post_evaluation_hook'):
      self.red_agent.post_evaluation_hook()
    if has_method(self.blue_agent, 'post_evaluation_hook'):
      self.blue_agent.post_evaluation_hook()
