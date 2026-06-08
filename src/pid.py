import queue
import threading
import time

import sensor

sensor_values_mid = queue.Queue()
sensor_values_right = queue.Queue()
sensor_values_left = queue.Queue()

average_mid = 0
average_right = 0
average_left = 0


def get_value_sensor_in_list_mid(
    sensor_function,
    readin_timestep_in_ms,
    number_of_values_to_readin,
):
    global sensor_values_mid

    while True:
        sensor_value_of_func = sensor_function("mid")
        number_of_values = sensor_values_mid.qsize()
        if sensor_value_of_func:
            sensor_value_converted = 1
        else:
            sensor_value_converted = 0

        if number_of_values < number_of_values_to_readin:
            sensor_values_mid.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)
        elif number_of_values >= number_of_values_to_readin:
            sensor_values_mid.get()
            sensor_values_mid.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)


def get_value_sensor_in_list_right(
    sensor_function,
    readin_timestep_in_ms,
    number_of_values_to_readin,
):
    global sensor_values_right

    while True:
        sensor_value_of_func = sensor_function("right")
        number_of_values = sensor_values_right.qsize()
        if sensor_value_of_func:
            sensor_value_converted = 1
        else:
            sensor_value_converted = 0

        if number_of_values < number_of_values_to_readin:
            sensor_values_right.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)
        elif number_of_values >= number_of_values_to_readin:
            sensor_values_right.get()
            sensor_values_right.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)


def get_value_sensor_in_list_left(
    sensor_function,
    readin_timestep_in_ms,
    number_of_values_to_readin,
):
    global sensor_values_left

    while True:
        sensor_value_of_func = sensor_function("left")
        number_of_values = sensor_values_left.qsize()
        if sensor_value_of_func:
            sensor_value_converted = 1
        else:
            sensor_value_converted = 0

        if number_of_values < number_of_values_to_readin:
            sensor_values_left.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)
        elif number_of_values >= number_of_values_to_readin:
            sensor_values_left.get()
            sensor_values_left.put(sensor_value_converted)
            time.sleep((readin_timestep_in_ms / number_of_values_to_readin) / 100)


def calc_average_value(values_list, orientation):
    while True:
        number_to_divide = values_list.qsize()
        if orientation == "right" and number_to_divide > 0:
            global average_right
            average_right = round(sum(list(values_list.queue)) / number_to_divide, 1)
        elif orientation == "left" and number_to_divide > 0:
            global average_left
            average_left = round(sum(list(values_list.queue)) / number_to_divide, 1)
        elif orientation == "mid" and number_to_divide > 0:
            global average_mid
            average_mid = round(sum(list(values_list.queue)) / number_to_divide, 1)


values_to_process_mid = threading.Thread(
    target=get_value_sensor_in_list_mid,
    args=(sensor.sensor_line, 10, 5),
)

values_to_process_right = threading.Thread(
    target=get_value_sensor_in_list_right,
    args=(sensor.sensor_line, 10, 5),
)

values_to_process_left = threading.Thread(
    target=get_value_sensor_in_list_left,
    args=(sensor.sensor_line, 10, 5),
)

calculate_average_mid = threading.Thread(
    target=calc_average_value, args=(sensor_values_mid, "mid")
)

calculate_average_right = threading.Thread(
    target=calc_average_value, args=(sensor_values_right, "right")
)

calculate_average_left = threading.Thread(
    target=calc_average_value, args=(sensor_values_left, "left")
)


# values_to_process_mid.start()
# calculate_average_mid.start()

# values_to_process_right.start()
# calculate_average_right.start()

# values_to_process_left.start()
# calculate_average_left.start()
