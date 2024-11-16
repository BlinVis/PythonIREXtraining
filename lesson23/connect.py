import streamlit as st
import requests
import pandas as pd

st.title('Project management app')
st.header('ass a developer')
dev_name=st.text_input('Developer name')
dev_experience=st.number_input('Experience years',min_value=0,max_value=50,value=0)
if st.button('create developer'):
    dev_data={'name':dev_name,'experience':dev_experience}
    response=requests.post('http://localhost:8000/developers/',json=dev_data)
    st.json(response.json())

st.header('Project dashboard')
if st.button('get projects'):
    response=requests.get('http://localhost:8000/developers/')
    projects_data=response.json()['projects']
    if projects_data:
        projects_df=pd.DataFrame(projects_data)

        st.subheader('projects overview')
        st.dataframe(projects_df)

        st.subheader('Project details')
        for project in projects_data:
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Languages used:**{' ,'.join(project['languages'])}")
            st.markdown(f"**Lead Developer:** {project['lead_developer']['name']}with {project['lead_developer']['experience']} years of experience")
            st.markdown("---")
        else:
            st.warning('No projects found!')
            

