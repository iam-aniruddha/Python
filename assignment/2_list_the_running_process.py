"""
# II. Write a Program 
# 1. to find all the list of all running process in your System
# 2. Display the count of each running process.
# 3. Store this information in a CSV File.
"""

import csv
import psutil

# Get list of running processes
processes = psutil.process_iter()

# Count the number of instances of each process
process_count = {}
for process in processes:
    name = process.name()
    if name in process_count:
        process_count[name] += 1
    else:
        process_count[name] = 1

# Print the count of each running process
for name, count in process_count.items():
    print(f"{name}: {count}")

# Store the information in a CSV file
with open('process_count.csv', mode='w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Process Name', 'Count'])
    for name, count in process_count.items():
        writer.writerow([name, count])
