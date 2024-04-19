from fastapi import FastAPI, Request ,APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI()


#app.mount("/", StaticFiles(directory="static", html=True), name="static")

# class lense:
#     def __init__(self):
#         pass

#     def start(self):
#         uvicorn.run("lense.app:app", reload=False, host="127.0.0.1", port=8889,workers=1)

        

@app.get("/test/")
async def test():
    print("*"*100)
    print("Inside the test")
    response ={}
    response["test"] = "testing"
    return  response

@app.post("/sum/")
async def sum1(a:int,b:int):
    print("*"*100)
    print("Inside the sum")
    response ={}
    response["sum"] = a+b
    return  response

def start():
    print("*"*100)
    print("Inside the start function ")
    print(__name__)
    import os
    app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
    uvicorn.run("lense.main:app", reload=False, host="127.0.0.1", port=9001,workers=1)