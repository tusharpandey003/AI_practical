import pandas as pd
import numpy as np
print("Hello !")
date = input("Give me  a date:")
month = input("which month:")
year = input("year:")

if month == "jan":
    d = np.random.randint(9, 15)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "feb":
    d = np.random.randint(15, 20)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "march":
    d = np.random.randint(18, 24)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "april":
    d = np.random.randint(20, 30)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "may":
    d = np.random.randint(30, 40)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "june":
    d = np.random.randint(35, 45)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "july":
    d = np.random.randint(30, 40)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "august":
    d = np.random.randint(30, 40)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "sept":
    d = np.random.randint(25, 35)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "oct":
    d = np.random.randint(20, 29)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "nov":
    d = np.random.randint(18, 22)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
if month == "dec":
    d = np.random.randint(15, 21)
    print(f"Temperature on {date} {month} {year} is {d} degree celcius.")
