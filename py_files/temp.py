import pandas as pd
import numpy as np
import plotly.express as px


# Define the start and end date for the DataFrame
start_date = '2023-01-01'
end_date = '2023-12-31'

# Generate a date range
date_range = pd.date_range(start_date, end_date)

# Initialize the DataFrame
df = pd.DataFrame()
df['Date'] = date_range

# Function to generate linearly increasing temperatures


def generate_temperature(date):
    month = date.month
    day = date.day
    # Define temperature range for each month (example ranges)
    base_temp = {
        1: 10,   # January
        2: 14,   # February
        3: 18,   # March
        4: 23,   # April
        5: 29,   # May
        6: 36,   # June
        7: 43,   # July
        8: 40,   # August
        9: 37,   # September
        10: 34,  # October
        11: 27,  # November
        12: 19   # December
    }
    # Generate a random deviation within [-3, 3]
    deviation = np.random.randint(-3, 3)
    if month <= 3:
        r = day*0.1
    elif month < 7:
        r = day*0.2
    else:
        r = day * (-0.2)

    # Add seasonal variation using sine and cosine functions
    seasonal_variation = 5 * np.sin(2 * np.pi * (month - 1) / 12)

    # Calculate the temperature for the day
    temperature = base_temp[month] + seasonal_variation+deviation+r
    return temperature


# Apply the function to the 'Date' column to create 'Temperature' column
df['Temperature'] = df['Date'].apply(generate_temperature)
print(df)

# # Display the DataFrame
# df.to_csv("day.csv")

# # Plot the temperature trend
# plt.figure(figsize=(10, 6))
# plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='b')
# plt.xlabel('Date')
# plt.ylabel('Temperature (°C)')
# plt.title('Temperature Trend (2024)')
# plt.grid(True)
# plt.show()

fig = px.line(df, x='Date', y="Temperature")
fig.write_html("temp.html")
