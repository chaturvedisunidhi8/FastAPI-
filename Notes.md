 http://127.0.0.1:8000    --- this is basically our local server ,
 127.0.0.1 :  Ip address of our local system by default same of everysystem
 8000      : it is port number means from which port your browser and other device will take entry
             and we can change this port number.



what is Endpoint :specific URL where an application send request  and receive response  

get("pass path here") is basically an HTTP method which is used to get the data from the server
get () is a by default HTTP method which sends data from backend to frontend or send API response

Note: in your FastAPI project, same routes never repeat otherwise ,syetm will confuse to retuen response 


http://127.0.0.1:8000/1 cant i give path parameter like this
from fastapi import FastAPI

app = FastAPI()

@app.get("/{id}")
def get_item(id: int):
    return {"id": id}



for Query Parameter

 from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }   



