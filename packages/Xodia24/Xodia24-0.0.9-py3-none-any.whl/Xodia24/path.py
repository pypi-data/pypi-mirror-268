import math

def distance_of_bullet(action, tank_positions):
    power, angle = action[0], action[1]
    angle_radians = math.radians(angle)
    time_of_flight = 2 * power * math.sin(angle_radians) / 9.8
    distance = time_of_flight * power * math.cos(angle_radians)
    diff_distance = round(abs(distance - tank_positions[1] + tank_positions[0]))
    return diff_distance

