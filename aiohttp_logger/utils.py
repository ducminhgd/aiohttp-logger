import os
import time


def cleanup(day_keep_alive, file_name):
    log_dir = os.path.dirname(file_name)
    current_time = time.time()
    day_conversion_unit = 24 * 3600
    for f in os.listdir(log_dir):
        if not f.endswith('.log'):
            continue
        file_path = os.path.join(log_dir, f)
        modified_time = os.path.getctime(file_path)
        if (current_time - modified_time) // day_conversion_unit <= day_keep_alive:
            continue
        os.unlink(file_path)
