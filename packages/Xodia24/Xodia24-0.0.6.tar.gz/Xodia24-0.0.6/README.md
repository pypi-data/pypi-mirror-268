# Xodia24: PocketTank Environment

<p  align="center">
<img src="https://i.ibb.co/P4nyZNv/Xodia-Logo-removebg-preview.png" alt="Xodia-Logo-removebg-preview" border="0" width="400px">
</p>
  

Xodia24 is a Python package providing a custom environment for simulating a tank battle scenario where two tanks are positioned on a 2D grid. The objective is to train a Reinforcement Learning (RL) agent to effectively control one of the tanks and shoot at the other tank using different actions such as adjusting power, angle, and moving the tank.

## Installation

You can install Xodia24 via pip:

```
pip install Xodia24
```

## Usage

1. **Implementing the Custom Reward Function:**
   Before training the RL model, it's necessary to implement the reward function according to specific problem requirements. This function should take the difference in distance between the bullet and the target tank as input and return the reward. To implement the custom reward function, you need to subclass the `PocketTank` environment and override the `reward` method with your custom implementation.

2. **Training the RL Model:**
   After implementing the custom reward function, you can train your RL model using this environment by interacting with it through the `step()` method. Provide actions to the tank and observe the resulting state, reward, and other information.

Example:
```python
# Import the environment
from Xodia24.env import PocketTank


# Train RL model using the environment
# ...
```


## Dependencies

- `gymnasium`: A toolkit for developing and comparing reinforcement learning algorithms.
- `numpy`: Library for numerical computations and array operations.
- `matplotlib`: Library for creating plots and visualizations.

## Implementation Note

If the custom reward function is not implemented, the default behavior will set the reward to 0. It's essential to implement a meaningful reward function tailored to the specific problem requirements for effective training of the RL model.

## Custom PocketTank Environment

To implement a custom reward function and use it in the PocketTank environment, you can utilize the `CustomPocketTank` class. Below is a code template for `CustomPocketTank`:

```python
# custom_reward.py

from Xodia24.env import PocketTank

# Import the PocketTank class and inherit from it to override the reward function
class CustomPocketTank(PocketTank):
    def __init__(self):
        super().__init__()

    # Override the reward function with your custom implementation
    def reward(self, action, diff_distance):
        """
        Custom reward function implementation.

        Args:
            action (np.ndarray): Array representing the action taken by the agent.
            diff_distance (float): Difference in distance between the bullet and the target tank.

        Returns:
            float: Custom reward value based on the difference in distance.
        """
        # Implement your custom reward logic here
        custom_reward = 0  # Modify this according to your requirements
        return custom_reward

# Train RL Model
```

### Action Space

The action space in the Xodia24 PocketTank environment refers to the set of possible actions that the reinforcement learning (RL) agent can take at each time step. In the tank battle scenario, the agent controls one of the tanks and has several actions available to it, including adjusting the power and angle of the tank's cannon and moving the tank across the 2D grid.

#### Available Actions:
- **Adjust Power**: The agent can adjust the power setting of the tank's cannon, determining the force with which the projectile is fired.
- **Adjust Angle**: The agent can adjust the angle of the tank's cannon, controlling the direction in which the projectile is launched.
- **Move Tank**: The agent can move the tank across the 2D grid, changing its position on the battlefield.

The action space is typically represented as a discrete or continuous space, depending on the specific implementation of the environment.

### Observation Space

The observation space refers to the information that the RL agent receives from the environment at each time step. This information helps the agent make decisions about which actions to take in order to achieve its objective. In the Xodia24 PocketTank environment, the observation space includes various features of the battlefield and the tanks' positions.

#### Example Observations:
- **Tank Positions**: The coordinates of both the agent-controlled tank and the opponent tank on the 2D grid.
- **Terrain Information**: Information about the terrain features, such as obstacles or cover, that may affect the trajectory of the projectile.
- **Projectile Position**: The current position of the projectile fired by the tanks.

The observation space can be represented as a vector, matrix, or other data structure depending on the complexity of the environment and the information that needs to be conveyed to the agent.


