from pydantic import BaseModel

class AuthorBase(BaseModel):
    name:str
class AuthorCreate(AuthorBase):
    pass


class Author_response(BaseModel):
    id:int
    name:str

class Author(AuthorBase):
    id:int


