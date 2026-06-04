import threading
import time

import motor
import pid
import sensor

motor.init()


def stop_all_wheels():
    motor.front_left(0)
    motor.front_right(0)
    motor.rear_left(0)
    motor.rear_right(0)


def turn_right(turn_speed_right, turn_speed_left):
    right_wheel_speed = 0
    left_wheel_speed = 0

    if (
        turn_speed_right > turn_speed_left
        and 0 <= abs(turn_speed_left) <= 100
        and 0 < abs(turn_speed_right) <= 100
    ):
        right_wheel_speed = int(turn_speed_right)
        left_wheel_speed = int(turn_speed_left)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)


def turn_left(turn_speed_left, turn_speed_right):
    right_wheel_speed = 0
    left_wheel_speed = 0
    if (
        """turn_speed_left > turn_speed_right"""
        and 0 < abs(turn_speed_left) <= 100
        and 0 <= abs(turn_speed_right) <= 100
    ):
        right_wheel_speed = int(turn_speed_right)
        left_wheel_speed = int(turn_speed_left)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)


def drive_straight(drive_speed, direction):
    drive_speed_direction = 0
    if direction == "f":
        drive_speed_direction = abs(drive_speed)
    elif direction == "r":
        drive_speed_direction = (-1) * abs(drive_speed)
    else:
        drive_speed_direction = 0

    motor.front_left(drive_speed_direction)
    motor.front_right(drive_speed_direction)
    motor.rear_left(drive_speed_direction)
    motor.rear_right(drive_speed_direction)


def line_detection_start_driving():
    while True:
        print(pid.average_left)
        if (
            not sensor.sensor_line("left")
            and not sensor.sensor_line("right")
            and sensor.sensor_line("mid")
        ):
            drive_straight(100 * pid.average_mid, "f")
            time.sleep(0.1)
            stop_all_wheels()
        elif not sensor.sensor_line("left") and sensor.sensor_line("right"):
            turn_left(100 * pid.average_left, 0)
        elif sensor.sensor_line("left") and not sensor.sensor_line("right"):
            turn_right(100 * pid.average_right, 0)
        elif (
            sensor.sensor_line("left")
            and sensor.sensor_line("right")
            and sensor.sensor_line("mid")
        ):
            stop_all_wheels()


"""Hier weiterarbeiten und die geradeaus fahrt sinnvoll einbauen.
ACHTUNG!!!: elektronikfehler Motoren gehen aus da Datenmenge wahrscheinlich zu groß"""


def scaled_right_left():
    while True:
        wheel_right = (-100 * pid.average_right) + 100
        wheel_left = (-100 * pid.average_left) + 100
        print(pid.average_right, pid.average_left)
        turn_left(wheel_left, wheel_right)


start_driving = threading.Thread(target=line_detection_start_driving)
scaled = threading.Thread(target=scaled_right_left)

# start_driving.start()
scaled.start()
pid.values_to_process_mid.start()
pid.calculate_average_mid.start()
pid.values_to_process_right.start()
pid.calculate_average_right.start()
pid.values_to_process_left.start()
pid.calculate_average_left.start()
