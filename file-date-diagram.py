import os
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter

# Step 1: Specify the directory
directory_path = input("Where are your files? ")

# Step 2: Collect modified dates
modified_dates = []

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # Get the last modified time and convert it to a date
            modified_time = os.path.getmtime(file_path)
            modified_date = datetime.fromtimestamp(modified_time).date()
            modified_dates.append(modified_date)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Step 3: Count occurrences of each date
date_counts = Counter(modified_dates)

# Step 4: Sort data by date
sorted_dates = sorted(date_counts.items())

# Extract dates and counts
dates, counts = zip(*sorted_dates)

# Step 5: Plot the data
plt.figure(figsize=(10, 6))
plt.bar(dates, counts, color='skyblue', edgecolor='black')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Files Modified", fontsize=12)
plt.title("File Modifications Over Time", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
