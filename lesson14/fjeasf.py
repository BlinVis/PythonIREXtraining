import pandas as pd

df = pd.read_csv('weather_tokyo_data.csv')
print(df.info())

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
avgTemperature = df['temperature'].mean()
roundedAvgTemperature = round(avgTemperature, 2)
print(f"This is the temperature asked on question 1: {roundedAvgTemperature}")

df['day'] = pd.to_datetime(df['day'], format="%m/%d")
df['month'] = df['day'].dt.month

monthly_avg_temperature = df.groupby("month")['temperature'].mean()
print(f"This is the temperature asked on question 2: {monthly_avg_temperature}")

import matplotlib.pyplot as plt

monthly_avg_temperature.plot(kind='bar', color='skyblue')
plt.title("Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.show()

# Identify the hottest and coldest days
hottest_day = df.loc[df['temperature'].idxmax()]
coldest_day = df.loc[df['temperature'].idxmin()]

print("Coldest Day:\n", coldest_day)
print("Hottest Day:\n", hottest_day)

plt.figure(figsize=(12, 6))
plt.plot(df['day'], df['temperature'])
plt.grid(True)
plt.show()



