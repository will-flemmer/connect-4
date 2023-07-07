from ..board import Board
from . import BoardEvaluator
from ..agent import Agent
from ..setup_test_env import setup_test_env

def test_setup():
  test_env = setup_test_env()
  return {
    'board_evaluator': BoardEvaluator(test_env['lcm'].board, test_env['red_agent'], test_env['blue_agent']),
    'red_agent': test_env['red_agent'],
    'blue_agent': test_env['blue_agent'],
    'board': test_env['lcm'].board
  }

def test_can_spot_a_horizontal_win():
  setup = test_setup()
  evaluator = setup['board_evaluator']
  red_agent = setup['red_agent']
  board = setup['board']

  board.grid[0][0] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 0})
  assert result['completed'] == False

  board.grid[0][1] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 1})
  assert result['completed'] == False

  board.grid[0][2] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 2})
  assert result['completed'] == False

  board.grid[0][3] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 3})
  assert result['completed'] == True
  assert result['winner'] == red_agent

def test_does_not_count_a_horizontal_win_if_not_connected():
  setup = test_setup()
  evaluator = setup['board_evaluator']
  red_agent = setup['red_agent']
  board = setup['board']

  board.grid[0][0] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 0})
  assert result['completed'] == False

  board.grid[0][1] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 1})
  assert result['completed'] == False

  board.grid[0][2] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 2})
  assert result['completed'] == False

  board.grid[0][4] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 3})
  assert result['completed'] == False

def test_can_spot_a_vertical_win():
  setup = test_setup()
  evaluator = setup['board_evaluator']
  blue_agent = setup['blue_agent']
  board = setup['board']

  board.grid[1][0] = 'B'
  board.grid[2][0] = 'B'
  board.grid[3][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 0})
  assert result['completed'] == False

  board.grid[4][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 0})
  assert result['completed'] == True
  assert result['winner'] == blue_agent

def test_can_spot_a_positive_diagonal_win():
  setup = test_setup()
  evaluator = setup['board_evaluator']
  blue_agent = setup['blue_agent']
  board = setup['board']

  board.grid[1][0] = 'B'
  board.grid[2][1] = 'B'
  board.grid[3][2] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 2})
  assert result['completed'] == False

  board.grid[4][3] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 3})
  assert result['completed'] == True
  assert result['winner'] == blue_agent

def test_can_spot_a_negative_diagonal_win():
  setup = test_setup()
  evaluator = setup['board_evaluator']
  blue_agent = setup['blue_agent']
  board = setup['board']

  board.grid[1][3] = 'B'
  board.grid[2][2] = 'B'
  board.grid[3][1] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 1})
  assert result['completed'] == False

  board.grid[4][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 0})
  assert result['completed'] == True
  assert result['winner'] == blue_agent