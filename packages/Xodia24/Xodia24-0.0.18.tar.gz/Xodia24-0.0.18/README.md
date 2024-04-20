# Xodia24: PocketTank Environment

<p align="center">
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

3. **Using the Custom PocketTank Environment:**
   If you want to utilize a custom implementation of the PocketTank environment, you can create your subclass and override the necessary methods. Here's a sample implementation:
   
# Custom PocketTank
```python
from Xodia24.env import PocketTank
from gymnasium import spaces
import numpy as np

class CustomPocketTank(PocketTank):
    def __init__(self):
        super().__init__()
        """
        Define a custom action space but only limit it
        dont change actual crux or step function wont work
         """
        # Example 1
		self.action_space  =  spaces.MultiDiscrete([100,90,1]) # This limit movement only hit from the current position
		# Example 2
		self.action_space  =  spaces.MultiDiscrete([100,45,3]) # Limit the angle
		# Example 3
		self.action_space  =  spaces.MultiDiscrete([60,90,3])# Limit the power of firing
    def reward(self, diff_distance):
        """
        Custom reward function implementation.

        Args:
            diff_distance (float): Difference in distance between the bullet and the target tank.

        Returns:
            float: Custom reward value based on the difference in distance.
        """
        # Implement your custom reward logic here
        custom_reward = 0 # Add your reward Function
        return custom_reward
```

## Dependencies

- `gymnasium`: A toolkit for developing and comparing reinforcement learning algorithms.
- `numpy`: Library for numerical computations and array operations.
- `matplotlib`: Library for creating plots and visualizations.


## Action Space

The action space in the Xodia24 PocketTank environment refers to the set of possible actions that the reinforcement learning (RL) agent can take at each time step. In the tank battle scenario, the agent controls one of the tanks and has several actions available to it, including adjusting the power and angle of the tank's cannon and moving the tank across the 2D grid.

### Available Actions:
- **Adjust Power**: The agent can adjust the power setting of the tank's cannon, determining the force with which the projectile is fired.
Range: 0-100
- **Adjust Angle**: The agent can adjust the angle of the tank's cannon, controlling the direction in which the projectile is launched.
Range: 0 deg - 90 deg
- **Move Tank**: The agent can move the tank across the 2D grid, changing its position on the battlefield.
0 = Dont move only fire
1 = move +25 and then fire
2 = move -25 and then fire


The action space is typically represented as a discrete or continuous space, depending on the specific implementation of the environment.

## Observation Space

The observation space refers to the information that the RL agent receives from the environment at each time step. This information helps the agent make decisions about which actions to take in order to achieve its objective. In the Xodia24 PocketTank environment, the observation space includes various features of the battlefield and the tanks' positions.

obs = [x1,x2,b]

x1: Your Tank Location
x2: Enemy Tank Location
b : bullet type ID



## Bullet Types

The tank has seven different types of bullets available, each with unique properties and effects. The tank has access to each bullet type an unlimited number of times.

1. *Standard Shell*:
    - *Description*: A classic projectile bullet that follows projectile motion.
    - *Damage*: Deals 20 damage upon hitting the target.
    - *Trajectory*: Parabolic trajectory determined by initial angle and velocity.
    - *ID*: 0

2. *Triple Threat*:
    - *Description*: A bullet that splits into three smaller bullets upon firing.
    - *Damage*: Each of the three bullets deals 20 damage, similar to the Standard Shell.
    - *Trajectory*: Parabolic trajectory similar to Standard Shell.
     - *ID*: 1

3. *Long Shot*:
    - *Description*: A bullet that deals more damage based on the distance it travels before hitting the ground.
    - *Damage*: Damage increases as the distance traveled increases.
    - *Trajectory*: Parabolic trajectory similar to the Standard Shell.
    - *ID*: 2

4. *Heavy Impact*:
    - *Description*: A high-damage bullet with limited range and velocity.
    - *Damage*: Deals 40 damage upon hitting the target.
    - *Trajectory*: Limited velocity and range compared to other bullets.
    - *ID*: 3

5. *Blast Radius*:
    - *Description*: A bullet that causes area damage within a radius of 100.
    - *Damage*: Deals 10 damage in a radius of 100 around the impact point.
    - *Trajectory*: Parabolic trajectory similar to the Standard Shell.
    - *ID*: 4

6. *Healing Halo*:
    - *Description*: A bullet that heals the tank upon impact.
    - *Healing*: Heals the tank by 10 points upon hitting the ground or a target.
    - *Trajectory*: Parabolic trajectory similar to the Standard Shell.
    - *ID*: 5

7. *Boomerang Blast*:
    - *Description*: A bullet that follows a unique trajectory resembling a boomerang.
    - *Damage*: Deals 20 damage upon hitting the target.
    - *Trajectory*: Follows a curved trajectory that slightly reverses direction, like a boomerang.
    - *ID*: 6

