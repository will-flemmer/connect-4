### Installation

```
pip install connect-four-game
```

## Usage

### Human vs Human
```python
from connect_four_game import Game, Agent

if __name__ == '__main__':
  red_agent = Agent('RED TEAM', 'red')
  blue_agent = Agent('BLUE TEAM', 'blue')
  lcm = Game(red_agent, blue_agent)
  lcm.start_game()
```

### AI vs AI
```python
from connect_four_game import Game

if __name__ == '__main__':
  red_rl_agent = RLAgent('red') # RLAgent is not included in the package
  blue_rl_agent = RLAgent('blue')
  game = Game(red_rl_agent, blue_rl_agent, row_count=ROW_COUNT, column_count=COLUMN_COUNT)
  game.start_game()
```

#### Example of RLAgent which chooses random action

```python
import random
from connect_four_game import BaseAgent
import numpy as np

class RLAgent(BaseAgent):
  def __init__(self, color: str, initial_exploration_rate=0.9):
    self.name = f'RL-Agent-{color.capitalize()}'
    self.color = color
    self.symbol = color[0].capitalize()

  def choose_action(self):
    return random.randint(0, len(self.game.grid[0]) - 1)

  def place_block(self):
    column = self.choose_action()
    return self.board.place_block(column, self.symbol)

  def post_evaluation_hook(self):
    print('This method is called after each move has been evaluated')
```

### Human vs AI
On the way...


