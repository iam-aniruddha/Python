""" 
This module contains a function to monitor the number
of instances of a given process and kill the oldest instance
if the maximum number of instances is exceeded. 
"""
import psutil
import decorator

instance = []

@decorator.log_decorator
def monitor_app(process_name, max_instnace):
    """
    :param process_name: The name of the app to monitor.
    :param max_instances: The maximum number of instances allowed for the app.
    :return: None
    """
    for p in psutil.process_iter(['pid','name']):
        if p.info['name'] == process_name:
            instance.append(p)

    if len(instance) > max_instnace:
        print(f"Killing {process_name} (more than {max_instnace})")
        # Kill the oldest process
        instance[0].kill()
        print("Done.")
    else:
        print(f"Number of instances of {process_name}: {len(instance)}")

# Monitoring a single app with maximum 2 instances
monitor_app('notepad.exe', 2)
