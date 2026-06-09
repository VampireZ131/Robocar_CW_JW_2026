import time

import sensor_new

last_pos_for_pid = 0.0
integral = 0.0


def pid_speed_calculation(detected_error, base_speed, kp, ki, kd):
    global last_pos_for_pid, integral

    integral_reset = 0

    value_sensor_right = sensor_new.pos_sensor_over_line("right")
    value_sensor_left = sensor_new.pos_sensor_over_line("left")
    value_sensor_mid = sensor_new.pos_sensor_over_line("mid")

    position = sensor_new.detect_error(
        value_sensor_left, value_sensor_mid, value_sensor_right
    )

    if position is None:
        position = last_pos_for_pid
        integral = integral_reset

    proportional = position
    integral = integral + position
    derivativ = last_pos_for_pid - position

    limited_integral = max(-20, min(20, integral))
    integral = limited_integral

    correction_factor = kp * proportional + ki * limited_integral + kd * derivativ

    speed_left = base_speed + correction_factor
    speed_right = base_speed - correction_factor

    last_pos_for_pid = position

    return speed_left, speed_right
