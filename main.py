#Lecture -2
#import fastapi
#print(fastapi.__version__)


from fastapi import FastAPI   #class

app=FastAPI()  #object


#Here how do we tell FastAPI that this is a fastapi route or Fstapi endpoint 
#so for that we will use 

#lecture -3

#http://127.0.0.1:8000
#@app.get("/")   #for which  route you want to use this function (/ slash means for home route or page)means after 8000 we will not pass any new path
#@app.get("/home")  #if you want to pass path after 8000 then you can use this,now this function will be called when we hit this path like http://127.0.0.8000/home

@app.get("/")
def Home():                       
    return "Welcome to FastAPI"

@app.get("/about")
def contact():
    return "FastAPI contact page"









