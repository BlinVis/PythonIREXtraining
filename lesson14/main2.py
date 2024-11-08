import pandas as pd
import matplotlib.pyplot as plt
import csv



df =pd.read_csv('avgIQpercountry.csv')
#print(df.info())

#subset=df[['Country','Average IQ']]
#filtered_df=subset[subset['Average IQ']>100]
#print(filtered_df)
#null_mask=df.isnull()
#null_count=null_mask.sum()
#print(f'the coudt is {null_count}')

#duplicated_count=df.duplicated().sum()
#print(f'the dup count is {duplicated_count}')
#df.drop_duplicates(keep='first', inplace=True)
#agregation functions
ave_iq_perc=df.groupby('Continent')['Average IQ'].mean()
print(ave_iq_perc.sort_values(ascending=False))


#visualisation


