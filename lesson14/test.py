import pandas as pd
import matplotlib.pyplot as plt



df =pd.read_csv('avgIQpercountry.csv')
filtered=df[df['Average IQ']>=0]
print(filtered.groupby('Continent')['Average IQ'].mean())
