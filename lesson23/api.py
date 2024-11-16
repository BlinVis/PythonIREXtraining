

from fastapi import FastAPI
from streamlit import title

from model import Developer, Project
app=FastAPI()
@app.post('/developer/')
def create_developer(dev:Developer):
    return {'message':'Developer created','developer':dev}
@app.post('/projects/')
def create_project(projekti:Project):
    return {'message':'Project created','projekti':projekti}

@app.get('/project/')
def get_projects():
    shembullProjekt=Project(
        title='Sample',

        description='this is fopsefhpoehf',
        languages=['PHP','JS'],
        lead_developer=Developer(name="Blin", experience=2)


    )
    return {'projects':[shembullProjekt]}


