import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv('avgIQpercountry.csv')
filtered=df[df['Average IQ']>=100]




ave_iq_perc=df.groupby('Continent')['Average IQ'].mean()
filtered=ave_iq_perc.sort_values( ascending=False)

#print(filtered)
plt.figure(figsize=(14 , 8))
#bars=plt.bar(filtered['Continent'],filtered['Average IQ'], color='skyblue')
#print(bars)
print(filtered[0])


