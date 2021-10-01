import csv

import matplotlib.pyplot as plt

filename = "Data_Visualization/data/sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #print(header_row)

    # for index, colum_header in enumerate(header_row):
        # 
        # print(index, colum_header)

    # Get high temperatures from this file.
    # highs = []
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c = "red")

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.show()