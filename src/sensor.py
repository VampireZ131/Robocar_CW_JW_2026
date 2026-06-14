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


def detect_position(sensor_left, sensor_mid, sensor_right):
    FULL_LEFT = -1.0
    HALF_LEFT = -0.5
    MID = 0.0
    HALF_RIGHT = -0.5
    FULL_RIGHT = 1.0
    if not sensor_left and sensor_mid and not sensor_right:
        return MID
    elif sensor_left and not sensor_mid and not sensor_right:
        return FULL_LEFT
    elif not sensor_left and not sensor_mid and sensor_right:
        return FULL_RIGHT
    elif sensor_left and sensor_mid and not sensor_right:
        return HALF_LEFT
    elif not sensor_left and sensor_mid and sensor_right:
        return HALF_RIGHT
