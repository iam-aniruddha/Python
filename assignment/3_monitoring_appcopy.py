# II. Write a program to monitor the applications running on your system. 
# To test: Execute any application like browser, notepad, calculator etc and make sure 
# that not more than 2 instances of the same application can be running.

import psutil

def monitor_application(process_name, max_instances):
    instances = [p for p in psutil.process_iter(['pid', 'name', 'create_time']) if p.info['name'] == process_name]
    instances = sorted(instances, key=lambda p: p.info['create_time'], reverse=True)  # Sort instances by creation time in reverse order

    if len(instances) > max_instances:
        print(f"Exceeded the maximum allowed instances of {process_name}")
        for i in range(max_instances, len(instances)):
            instances[i].terminate()  # Terminate the newest instances
    else:
        print(f"Number of instances of {process_name}: {len(instances)}")

# Example usage
monitor_application("notepad.exe", 2)

