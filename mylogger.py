#!/usr/bin/python

# Libraries
from datetime import datetime
import config


def logging(level, message_incoming):

    message = str(message_incoming)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    message_to_print = ''

    # Formatting output message
    if level == "error":
        message_to_print = dt_string + " - Error   - " + message

    elif level == "warning":
        message_to_print = dt_string + " - Warning - " + message

    elif level == "info":
        message_to_print = dt_string + " - Info    - " + message

    elif level == "debug":
        message_to_print = dt_string + " - Debug   - " + message
    else:
        print("SystemError: Logging with wrong level value (level = " + level + "/ message = " + message + ").")
        exit(50)

    # Printing and writing the output
    if (level in ["info", "error", "warning"]) or (config.DEBUG_MODE and level in ["debug"]):
        print(message_to_print)

        # if activated, writing output into a log file - refer config.py
        if config.logging_into_log_file_activation_flag:
            injection_text_into_file(get_log_file_name(), message_to_print)

    return 0


def print_blank_line(level):
    logging(level, " ")
    return 0


def brut_logging(message):
    print(message)
    return 0


def open_log_file(filename, mode):
    log_file_full_path = config.logging_folder + filename + config.logging_file_extension

    # Set how to open the log file
    if mode == config.LOG_FILE_APPEND:
        option_mode = config.LOG_FILE_APPEND_OPTION

    elif mode == config.LOG_FILE_WRITE:
        option_mode = config.LOG_FILE_WRITE_OPTION

    else:
        option_mode = config.LOG_FILE_APPEND_OPTION

    try:
        # Append to the file (or create one if necessary) due to the "a" option.
        file_object = open(log_file_full_path, option_mode)
    except FileNotFoundError as error:
        print("ERROR - Log file open operation failed - path = " + log_file_full_path)
        print("Error details:" + str(error.args))
        exit(90)

    return file_object


def close_log_file(file_object):
    file_object.close()
    return 0


def write_into_log_file(filename, text_to_insert):
    filename.write(text_to_insert + '\n')
    return 0


def injection_text_into_file(log_file_name, message):
    my_file = open_log_file(log_file_name, config.LOG_FILE_APPEND)
    write_into_log_file(my_file, message)
    close_log_file(my_file)
    return 0


def reset_log_file(log_file_name):
    my_file = open_log_file(log_file_name, config.LOG_FILE_WRITE)
    write_into_log_file(my_file, '')
    close_log_file(my_file)
    return 0


def get_log_file_name():
    now = datetime.now()
    dt_string_log_file = now.strftime("%Y%m%d")

    return dt_string_log_file


def get_datetime():

    now = datetime.now()
    datetime_str = now.strftime(config.JOB_SUMMARY_DATETIME_FORMAT)

    return datetime_str


def get_time_spent_in_minutes(job_selected, start_date, end_date):

    diff = datetime.strptime(end_date, config.JOB_SUMMARY_DATETIME_FORMAT) - datetime.strptime(start_date, config.JOB_SUMMARY_DATETIME_FORMAT)
    diff_minutes = int(diff.seconds)/60

    print_blank_line('info')
    logging('info', 'JOB SUMMARY | ' + str(job_selected) + ' took at total: ' + str(diff_minutes) + ' minutes.')
    print_blank_line('info')
    print_blank_line('info')

    return 0


def job_starting(job_selected):
    print_blank_line('info')
    logging('info', 'JOB STARTING | ' + str(job_selected))
    print_blank_line('info')
    print_blank_line('info')

    return 0

