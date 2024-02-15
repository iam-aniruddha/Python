import psutil

instance = []
def monitor_app(process_name, max_instnace):
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