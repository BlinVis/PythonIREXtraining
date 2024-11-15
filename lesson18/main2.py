import pandas as pd
import streamlit as st
import plotly.express as px


books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')
st.title('best selling books analysis')
st.write('this app analyzes the amazon top selling books from 2009 to 2022')

st.subheader('summary statics')
total_books=books_df.shape[0]
unique_title=books_df['Name'].nunique()
avg_rating=books_df['User Rating'].mean()
avg_price=books_df['Price'].mean()

coll1,coll2,coll3,coll4=st.columns(4)

coll1.metric('total books',total_books)
coll2.metric('number of unique titles',unique_title)

coll3.metric('average rating',avg_rating)
coll4.metric('average price in dollars',avg_price)


col1,col2=st.columns(2)

with col1:
    st.subheader('top 10 book title')
    top_titles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader('top 10 book authors')
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader('Genre distribution')
fig=px.pie(books_df,names='Genre',title='Most liked genres',color='Genre',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
max_rating = books_df['User Rating'].max()

# Filter the dataset to get the book(s) with the maximum rating
best_rated_books = books_df[books_df['User Rating'] == max_rating]
top10_best_rated_books=best_rated_books.drop_duplicates(subset='Name').head(10)



# Display the result
fig = px.bar(
    top10_best_rated_books,
    x='Name',
    y='User Rating',
    color='User Rating',
    title='Best Rated Unique Books',
    labels={'Name': 'Book Title', 'User Rating': 'Rating'},
    color_continuous_scale='Viridis'
)

# Show the plot in the Streamlit app
st.plotly_chart(fig)

