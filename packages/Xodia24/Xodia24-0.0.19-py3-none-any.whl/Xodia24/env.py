
from gymnasium import Env, spaces
import random
import math
import numpy as np

class PocketTank(Env):
    def __init__(self):
        self.tank_1_positions_range = (50,150)
        self.tank_2_positions_range = (650,750)

        self.x1 = random.randint(*self.tank_1_positions_range)
        self.x2 = random.randint(*self.tank_2_positions_range)
        self.g = 12

        self.observation_space = spaces.MultiDiscrete([801,801,7])
        self.action_space = spaces.MultiDiscrete([100,90,3])

        self.action_cnt = 20
        self.remaining_actions = [self.action_cnt, self.action_cnt]

        self.v_wind = +8
        self.bullet_type = random.randint(0,6)

    def _get_boomerang_range(self, v, theta, g, air_factor = 7):
        theta = theta*math.pi/180
        if v*math.cos(theta)>0:
            dir = 1
        elif v*math.cos(theta)<0:
            dir = -1
        else:
            dir = 0
        range = (v**2)*math.sin(2*theta)/g - dir*0.5*air_factor*(v*math.cos(theta))**2/g**2
        return range
    
    def _get_range(self,action,tank,bullet_type):
        (v,angle,move) = action
        if(bullet_type==6):
            g = self.g
            range = self._get_boomerang_range(v,angle,g)
            return range
        if(bullet_type==5):
            v = min(50,v)
        rad_angle = math.radians(angle)
        vx = v * math.cos(rad_angle)
        vy = v * math.sin(rad_angle)
        if(tank==0):
            vx = vx + self.v_wind
        else : 
            vx = vx - self.v_wind
        
        range = ((2 * vy)/self.g) * vx
        return range

    def _get_bullet_position(self,action,tank,bullet_type):
        range = self._get_range(action,tank,bullet_type)
        x_bullet = 0 
        if(tank==0):
            x_bullet =  self.x1 + range
        else :
            x_bullet =  self.x2 - range
        return x_bullet

    def _get_diff(self,x_bullet,tank):
        diff = 0 
        if(tank==0):
            diff = abs(self.x2-x_bullet)
        else: 
            diff = abs(self.x1-x_bullet)
        return diff

    def _get_reward(self, diff, bullet_type):
        # reward = ....
        return 0

    def _check_for_end(self):
        if(self.remaining_actions == [0,0] or self.remaining_actions==[0,self.action_cnt]):
            return True
        else : 
            return False

    def _get_state(self):
        state = np.array([self.x1,self.x2,self.bullet_type])
        return state

    def _make_move(self,move,tank):
        if(tank==0):
            if(move==0):
                self.x1 = min(self.x1 + 25, 300)
            elif (move == 1):
                self.x1 = max(self.x1-25,0)
        else : 
            if(move==0):
                self.x2 = max(500,self.x2-25)
            elif(move == 1) : 
                self.x2 = min(798,self.x2+25)

    def step(self, action, tank=0):
        (v,angle,move) = action
        self._make_move(move,tank)
        bullet_type = self.bullet_type
        x_bullet = self._get_bullet_position(action,tank,bullet_type)
        diff = self._get_diff(x_bullet,tank)
        reward = self._get_reward(diff,bullet_type)
        
        self.remaining_actions[tank]-=1
        done = self._check_for_end()
        self.bullet_type = random.randint(0,6)
        state = self._get_state()
        info = {"reward":reward}
        truncated = False
        
        return (state,reward,done,truncated,info)

    def reset(self,seed=None, values = None):
        self.x1 = random.randint(*self.tank_1_positions_range)
        self.x2 = random.randint(*self.tank_2_positions_range)
        self.remaining_actions = [self.action_cnt, self.action_cnt]
        state = self._get_state()
        info = {}
        return (state,info)