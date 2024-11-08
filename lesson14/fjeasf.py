import  pandas as pd
df = pd.read_csv("weather_tokyo_data.csv")


year=df.groupby("year")["atmospheric pressure"].mean()
print(year)



