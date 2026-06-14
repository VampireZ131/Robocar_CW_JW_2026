import time

import sensor

last_pos_for_pid = 0.0
integral = 0.0


def pid_speed_calculation(refreshrate_in_Hz, base_speed, kp, ki, kd, ks):
    global last_pos_for_pid, integral

    integral_reset = 0
    sleep_time_refreshrate = 1 / refreshrate_in_Hz

    value_sensor_right = sensor.pos_sensor_over_line("right")
    value_sensor_left = sensor.pos_sensor_over_line("left")
    value_sensor_mid = sensor.pos_sensor_over_line("mid")

    position = sensor.detect_position(
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

    dynamic_base_speed = base_speed - (abs(position) * ks)
    speed_left = dynamic_base_speed + correction_factor
    speed_right = dynamic_base_speed - correction_factor

    last_pos_for_pid = position

    time.sleep(sleep_time_refreshrate)

    return speed_left, speed_right
