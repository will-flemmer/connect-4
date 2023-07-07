from . import Agent
from ..board import Board
from ..setup_test_env import setup_test_env

def test_can_place_block(monkeypatch):
  test_env = setup_test_env()
  agent = test_env['red_agent']

  monkeypatch.setattr('builtins.input', lambda _: "1")
  output = agent.place_block()
  assert output == { 'row': 5, 'column': 1 }
  output = agent.place_block()
  assert output == { 'row': 4, 'column': 1 }