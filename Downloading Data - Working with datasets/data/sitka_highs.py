import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = "sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # printing out the headers and their positions.
    # We see that the data we need which are the date & the max temperature is in the 2nd & the 5th col,
    # We'll process each row of data and extract the values at index 2 & 5 to visualize.

    """Get Dates & High Temperature from this file. """
    """Extracting & Reading Data."""
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5]) # Converting the string data in the TMAX col to integer before appending.
        dates.append(current_date)
        highs.append(high)
    print(highs)
    # We've extracted the high temperature data for each date and stored each value in a list. Now let's create a
    # visualisation of this data.

    # Plotting data in a temperature chart.
    fig,ax = plt.subplots()
    ax.plot(dates, highs, c="red")

    #Formatting the plot.
    plt.title("Daily High Temperatures, July 2018", fontsize=14)
    plt.xlabel("", fontsize=10)
    fig.autofmt_xdate() # Draws the dates on the x-axis.
    plt.ylabel("Temperature (F)", fontsize=10)
    plt.tick_params(axis="both", which="major", labelsize=10)
    plt.savefig("sitka_highs.png", bbox_inches="tight")
    plt.show()

    """The datetime module."""



