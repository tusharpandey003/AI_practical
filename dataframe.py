import numpy as np
import pandas as pd
dates = []
months = []
years = []
# 1.  january
jan_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month1 = ["jan"]
year = [2023]
temp1 = np.random.randint(8, 14, 31)
temp1 = pd.Series(temp1)

for x in year:
    for j in month1:
        for i in jan_dates:
            dates.append(i)
            months.append(j)
            years.append(x)
# 2. february
feb_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
month2 = ["feb"]
temp2 = np.random.randint(11, 20, 28)
temp2 = pd.Series(temp2)
year = [2023]
for x in year:
    for m in month2:
        for p in feb_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp1, temp2], ignore_index=True)

# 3. march
march_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month3 = ["march"]
temp3 = np.random.randint(17, 29, 31)
temp3 = pd.Series(temp3)
year = [2023]
for x in year:
    for m in month3:
        for p in march_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp3], ignore_index=True)
# 4. april
april_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
month4 = ["april"]
temp4 = np.random.randint(23, 36, 30)
temp4 = pd.Series(temp4)
year = [2023]
for x in year:
    for m in month4:
        for p in april_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp4], ignore_index=True)
# 5. may
may_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month5 = ["may"]
temp5 = np.random.randint(27, 43, 31)
temp5 = pd.Series(temp5)
year = [2023]
for x in year:
    for m in month5:
        for p in may_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp5], ignore_index=True)
# 6.june
june_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
month6 = ["june"]
temp6 = np.random.randint(30, 45, 30)
temp6 = pd.Series(temp6)
year = [2023]
for x in year:
    for m in month6:
        for p in june_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp6], ignore_index=True)
# july
july_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month7 = ["july"]
temp7 = np.random.randint(28, 35, 31)
temp7 = pd.Series(temp7)
year = [2023]
for x in year:
    for m in month7:
        for p in july_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp7], ignore_index=True)
# 8. august
august_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month8 = ["august"]
temp8 = np.random.randint(27, 34, 31)
temp8 = pd.Series(temp8)
year = [2023]
for x in year:
    for m in month8:
        for p in august_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp8], ignore_index=True)
# sept
sept_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
month9 = ["sept"]
temp9 = np.random.randint(25, 34, 30)
temp9 = pd.Series(temp9)
year = [2023]
for x in year:
    for m in month9:
        for p in sept_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp9], ignore_index=True)
# oct
oct_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month10 = ["oct"]
temp10 = np.random.randint(21, 33, 31)
temp10 = pd.Series(temp10)
year = [2023]
for x in year:
    for m in month10:
        for p in oct_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp10], ignore_index=True)
# nov
nov_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
month11 = ["nov"]
temp11 = np.random.randint(14, 28, 30)
temp11 = pd.Series(temp11)
year = [2023]
for x in year:
    for m in month11:
        for p in nov_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp11], ignore_index=True)
# dec
dec_dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month12 = ["dec"]
temp12 = np.random.randint(9, 20, 31)
temp12 = pd.Series(temp12)
year = [2023]
for x in year:
    for m in month12:
        for p in dec_dates:
            dates.append(p)
            months.append(m)
            years.append(x)
temp = pd.concat([temp, temp12], ignore_index=True)

ser1 = pd.Series(dates)
ser2 = pd.Series(months)
ser3 = pd.Series(years)
ser4 = pd.Series(temp)
df = pd.DataFrame({"date": ser1, "month": ser2, "year": ser3,
                  "temp(celcius)": ser4})
print(df)


# saving the dataframe
df.to_csv('file1.csv')
