import logging
import json
import time
import sys

performance_log = {}

# decorator to calculate process computation duration
def calculate_duration(func):
    def inner_method(*args, **kwargs):
        begin = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        performance_log[func.__name__ + '_duration'] = round((end - begin)*1000,2)
        return return_value
    return inner_method