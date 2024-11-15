import pandas as pd
import streamlit as st
import plotly.express as px



books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')
st.sidebar.header('Add new book data')
with st.sidebar.form('book_form'):
    new_name=st.text_input('Book Name')
    new_author=st.text_input('Author name')
    new_user_rating=st.slider('User rating',0.0,5.0,0.0,0.1)
    new_reviews=st.number_input('Review',min_value=0,step=1)
    new_price=st.number_input('Price',min_value=0,step=1)
    new_year=st.number_input('Year',min_value=2009,max_value=2022,step=1)
    new_genre=st.selectbox('Genre',books_df['Genre'].unique())
    submit_button=st.form_submit_button(label='Add new book')
if submit_button:
    new_data={
        'Name':new_name,
        'Author':new_author,
        'User Rating':new_user_rating,
        'Reviews':new_reviews,
        'Price':new_price,
        'Year':new_year,
        'Genre':new_genre
    }

    books_df=pd.concat([pd.DataFrame(new_data , index=[0]),books_df],ignore_index=True)

    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv',index=False)
    st.sidebar.success('New book added')

st.sidebar.header('Filter options:')
selected_author=st.sidebar.selectbox('Select Author',['All']+list(books_df['Author'].unique()))
selected_year=st.sidebar.selectbox('Select year',['All']+list(books_df['Year'].unique()))
selected_genre=st.sidebar.selectbox('Select Genre',['All']+list(books_df['Genre'].unique()))
min_rating=st.sidebar.slider('Minimum user rating',0.0,5.0,0.0,0.1)
max_price=st.sidebar.slider('Maximum Price',0,books_df['Price'].max(),books_df['Price'].max())

filtered_df=books_df.copy()
if selected_author!='All':
    filtered_df=filtered_df[filtered_df['Author']==selected_author]
if selected_year!='All':
    filtered_df=filtered_df[filtered_df['Year']==selected_year]

if selected_genre!='All':
    filtered_df=filtered_df[filtered_df['Genre']==selected_genre]

filtered_df=filtered_df[
    (filtered_df['User Rating']>=min_rating)&(filtered_df['Price']<=max_price)

]
st.title('best selling books analysis')
st.write('this app analyzes the amazon top selling books from 2009 to 2022')

st.subheader('summary statics')
total_books=filtered_df.shape[0]
unique_title=filtered_df['Name'].nunique()
avg_rating=filtered_df['User Rating'].mean()
avg_price=filtered_df['Price'].mean()

coll1,coll2,coll3,coll4=st.columns(4)

coll1.metric('total books',total_books)
coll2.metric('number of unique titles',unique_title)

coll3.metric('average rating',avg_rating)
coll4.metric('average price in dollars',avg_price)


col1,col2=st.columns(2)

with col1:
    st.subheader('top 10 book title')
    top_titles=filtered_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader('top 10 book authors')
    top_authors=filtered_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

#st.subheader('Genre distribution')
#fig=px.pie(filtered_df,names='Genre',title='Most liked genres',color='Genre',color_discrete_sequence=px.colors.sequential.Plasma)
#st.plotly_chart(fig)
#max_rating = filtered_df['User Rating'].max()

# Filter the dataset to get the book(s) with the maximum rating
#best_rated_books = filtered_df['User Rating'] == max_rating]
#top10_best_rated_books=best_rated_books.drop_duplicates(subset='Name').head(10)



# Display the result
#fig = px.bar(
    #filtered_df,
    #x='Name',
   # y='User Rating',
    #color='User Rating',
    #title='Best Rated Unique Books',
   # labels={'Name': 'Book Title', 'User Rating': 'Rating'},
   # color_continuous_scale='Viridis'
#)#

# Show the plot in the Streamlit app
#st.plotly_chart(fig)
st.subheader('Number of fiction vs Non fiction books over the years')
size=books_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig=px.bar(size,x='Year',
           y='Counts',
           color='Genre',
           title='Number of fiction vs non fiction books from 2009 to 2022',
           color_discrete_sequence=px.colors.sequential.Plasma,
           barmode='group'

           )
st.plotly_chart(fig)

#top 15 authors by counts of books published
st.subheader('top 15 authors by counts of books published')
top_authors=books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']
fig=px.bar(top_authors,
           x='Count',
           y='Author',
           orientation='h',
           title='Top 15 authors by counts of books published',
           labels={'Count':'Counts of books published','Author':'Author'},
           color='Count',
           color_continuous_scale=px.colors.sequential.Plasma
           )
st.plotly_chart(fig)

#Interactivity filter data by genre
st.subheader('Filter data by genre')
genre_filter=st.selectbox('Select genre',books_df['Genre'].unique())
filtered_df=books_df[books_df['Genre']==genre_filter]
st.write(filtered_df)










