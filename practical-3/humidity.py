import pandas as pd
import numpy as np


df = pd.read_csv("practical-2//day.csv")
df = df.drop(df.columns[0], axis=1)

df['Date'] = pd.to_datetime(df['Date'])


def generate_humidity(date):
    month = date.month
    # Define temperature ranges for each month (example ranges)
    humid_ranges = {
        1: (44, 75),   # January
        2: (37, 66),   # February
        3: (24, 52),   # March
        4: (15, 44),  # April
        5: (14, 41),  # May
        6: (30, 56),  # June
        7: (40, 79),  # July
        8: (60, 81),  # August
        9: (55, 85),  # September
        10: (40, 70),  # October
        11: (36, 70),  # November
        12: (49, 76)   # December
    }
    # Get the temperature range for the month
    temp_range = humid_ranges.get(month, (0, 10))
    # Generate a random temperature within the range
    return np.random.uniform(temp_range[0], temp_range[1])


x = df['Date'].apply(generate_humidity)
df['Humidity in percent'] = x.apply(lambda x: round(x, 2))
print(df)

df.to_csv("humidity.csv", index=False)
