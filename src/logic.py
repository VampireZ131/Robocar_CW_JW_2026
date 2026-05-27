import motor
import time
import sensor

motor.init()

def stop_all_wheels():
    motor.front_left(0)
    motor.front_right(0)
    motor.rear_left(0)
    motor.rear_right(0)

def turn_right(turn_speed, turn_radius):
    wheelbase_in_cm= 13
    right_wheel_speed=0
    left_wheel_speed=0
    turn_radius_scaled= turn_radius*0.1
    if 0< turn_radius_scaled <=10 and 0< turn_speed <=100:
        right_wheel_speed= int(((turn_speed * ((turn_radius_scaled + wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)
        left_wheel_speed= int(((turn_speed * ((turn_radius_scaled - wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)

def turn_left(turn_speed, turn_radius):
    wheelbase_in_cm= 13
    right_wheel_speed=0
    left_wheel_speed=0
    turn_radius_scaled= turn_radius*0.1
    if 0< turn_radius_scaled <=10 and 0< turn_speed <=100:
        right_wheel_speed= int(((turn_speed * ((turn_radius_scaled - wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)
        left_wheel_speed=  int(((turn_speed * ((turn_radius_scaled + wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)

def drive_straight(drive_speed, direction):
    drive_speed_direction=0
    if direction == "f":
        drive_speed_direction = abs(drive_speed)
    elif direction == "r":
        drive_speed_direction = (-1)*abs(drive_speed)
    else:
        drive_speed_direction = 0

    motor.front_left(drive_speed_direction)
    motor.front_right(drive_speed_direction)
    motor.rear_left(drive_speed_direction)
    motor.rear_right(drive_speed_direction)

def line_detection_start_driving():
    while True:
        if sensor.sensor_line("mid"):
            drive_straight(10, "f")
            time.sleep(0.2)
        elif sensor.sensor_line("right")
            turn_right(10, 10)
            time.sleep(0.2)
        elif sensor.sensor_line("left")
            turn_left(10, 10)
            time.sleep(0.2)
        else:
            stop_all_wheels()

line_detection_start_driving()
