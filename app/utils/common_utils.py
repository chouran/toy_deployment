import logging
import json
import time
import sys

performance_log = {}

#Creating and Configuring Logger
def console_logger(module_name):
    Log_Format = "[%(asctime)s] [%(levelname)s] ["+ module_name + "] - %(message)s"
    logging.basicConfig(stream = sys.stdout, 
                        filemode = "w",
                        format = Log_Format, 
                        level = service_info["log_level"])
    logger = logging.getLogger()
    return logger
    
# decorator to calculate process computation duration
def calculate_duration(func):
    def inner_method(*args, **kwargs):
        begin = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        performance_log[func.__name__ + '_duration'] = round((end - begin)*1000,2)
        return return_value
    return inner_method