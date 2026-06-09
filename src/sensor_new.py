import time

from gpiozero import LineSensor

linesensor_right = LineSensor(23)
linesensor_mid = LineSensor(15)
linesensor_left = LineSensor(14)


def pos_sensor_over_line(sensor_orientation):
    if sensor_orientation == "right":
        sensor_value_right = linesensor_right.value
        return sensor_value_right
    elif sensor_orientation == "left":
        sensor_value_left = linesensor_left.value
        return sensor_value_left
    else:
        sensor_value_mid = linesensor_mid.value
        return sensor_value_mid


def detect_error(sensor_left, sensor_mid, sensor_right):
    full_left = -1.0
    half_left = -0.5
    mid = 0.0
    half_right = -0.5
    full_right = 1.0
    if not sensor_left and sensor_mid and not sensor_right:
        return mid
    elif sensor_left and not sensor_mid and not sensor_right:
        return full_left
    elif not sensor_left and not sensor_mid and sensor_right:
        return full_right
    elif sensor_left and sensor_mid and not sensor_right:
        return half_left
    elif not sensor_left and sensor_mid and sensor_right:
        return half_right
