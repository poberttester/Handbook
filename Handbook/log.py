import time


def log_cash(some_str, result):
    with open('log.txt', 'a', encoding = 'utf-8') as file:
        named_tuple = time.localtime()
        time_string = time.strftime("[%m/%d/%Y, %H:%M:%S]", named_tuple)

        file.write(f'time: {time_string} event: {some_str} => {result} \n')