from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"Hello World"}


@app.get("/about")
def about():
    return{"name":"Fatima"}
@app.get("/contact")
def contact():
    return{"phone":"12345"}
@app.get("/students/{id}")
def students(id):
    return{"students ID":id}
@app.get("/students/{id}")
def student(id:int):
    return{"ID":id}
@app.get("/search")
def search(name:str):
    return{"Name":name}


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class student(BaseModel):
    name:str
    age:int
    email:str=None
@app.post("/student")
def create_student(student:student):
    return{"message":"student added","data":student}


from fastapi import FastAPI
app=FastAPI()
@app.get("/add")
def add(a:int,b:int):
    return{"Result":a+b}
@app.get("/subtract")
def subtract(a:int,b:int):
    return{"Result":a_b}
@app.get("/multiply")
def multiply(a:int,b:int):
    return{"Result":a*b}
@app.get("/divide")
def divide(a:int,b:int):
    return{"Result":a/b}


