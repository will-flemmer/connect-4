from .agent.agent import Agent
from .lifecycle_manager.lifecycle_manager import LifeCycleManager as Game

def setup_test_env():
  red_agent = Agent('RED TEAM', 'red')
  blue_agent = Agent('BLUE TEAM', 'blue')
  lcm = Game(red_agent, blue_agent)
  return { 'red_agent': red_agent, 'blue_agent': blue_agent, 'lcm': lcm}
