import numpy as np
import pandas as pd

date_rng = pd.date_range(start='1800-01-01', end='2023-05-25', freq='D')
df = pd.DataFrame({"Dates": date_rng})


# Function to generate random temperatures based on the month
def generate_temperature(date):
    month = date.month
    # Define temperature ranges for each month (example ranges)
    temp_ranges = {
        1: (8, 14),   # January
        2: (11, 20),   # February
        3: (17, 29),   # March
        4: (23, 35),  # April
        5: (34, 46),  # May
        6: (35, 47),  # June
        7: (32, 39),  # July
        8: (28, 38),  # August
        9: (25, 34),  # September
        10: (21, 33),  # October
        11: (14, 24),  # November
        12: (8, 17)   # December
    }
    # Get the temperature range for the month
    temp_range = temp_ranges.get(month, (0, 10))
    # Generate a random temperature within the range
    return np.random.uniform(temp_range[0], temp_range[1])


# Apply the function to the 'Date' column to create 'Temperature' column
x = df['Dates'].apply(generate_temperature)
df['Temperature in celsius'] = x.apply(lambda x: round(x, 2))
print(df)

# Display the DataFrame
df.to_csv('Delhi_temperature.csv')
print(df)
