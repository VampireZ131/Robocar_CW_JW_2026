import json
import os

import logic_new
import motor


def get_values_of_json(needed_value):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path_json_file = os.path.join(base_dir, "config_new.json")
    with open(path_json_file, "r") as config_file:
        config_data = json.load(config_file)
    return config_data[str(needed_value)]


def start_driving():
    motor.init()
    LIMITER_MAX = 100
    LIMITER_MIN = -100
    refreshrate = get_values_of_json("refreshrate in Hz")
    base_speed = get_values_of_json("base speed")
    kp = get_values_of_json("proportional factor")
    ki = get_values_of_json("integral factor")
    kd = get_values_of_json("derivativ factor")
    ks = get_values_of_json("dynamicspeed factor")

    while True:
        left_side_speed, right_side_speed = logic_new.pid_speed_calculation(
            refreshrate, base_speed, kp, ki, kd, ks
        )

        left_side_speed_limited = max(LIMITER_MIN, min(LIMITER_MAX, left_side_speed))
        right_side_speed_limited = max(LIMITER_MIN, min(LIMITER_MAX, right_side_speed))

        motor.front_left(left_side_speed_limited)
        motor.front_right(right_side_speed_limited)
        motor.rear_left(left_side_speed_limited)
        motor.rear_right(right_side_speed_limited)


start_driving()
