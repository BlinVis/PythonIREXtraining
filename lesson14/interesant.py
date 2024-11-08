import plotly.express as px
import pandas as pd
import matplotlib as plt
df=pd.read_csv('avgIQpercountry.csv')
df['Population - 2023']=df['Population - 2023'].str.replace(',','').astype(float)
print(df.info())
fig=px.scatter_geo(df, locations='Country', locationmode='country names',hover_name='Country', size='Average IQ',
                   color='Continent', projection='natural earth',title='Avg IQ per county',
                   size_max=20 , template='plotly_dark')
fig.show()


