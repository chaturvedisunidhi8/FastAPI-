#Lecture -4
from fastapi import FastAPI 
from MockData import products

app=FastAPI()  #object

@app.get("/products")
def get_products():
    return products


#Path Parameters
#@app.get("/products/{products_id}")                # input http://127.0.0.1:8000/products/1
#def get_products(products_id:int):                 # output will be product with id 1
#    return {
#        "id":products_id,
#    }



## Path Params
#@app.get("/products/{product_id}")
#def get_one_product(product_id: int):
#    ## if product available with the id, return product, else return error message.
#
#    for oneProduct in products:
#        if oneProduct.get("id") == product_id:
#            return oneProduct
#
#    return {
#        "error": "Product not Found for this ID."
#    }

#@app.get("/greet")
#def greet_user():
#    return "Hello User, Welcome to FastAPI"

@app.get("/greet")
def greet_user(name:str,age:int):                                    #suppose we want to greet user with his name, then we can use query params
    return {  
        "greet": f"Hello {name},and you are {age} years old."        #now whatever we will pass in path like http://127.0.0.1:8000/greet?name=John we will get output as Hello John, Welcome to FastAPI
    }

#def greet_user(name:str,age:int):   #this is fine but what if we get 300 data then 

@app.get("/greet")
def greet_user(name:str,age:int):                                    
        "greet": f"Hello {name},and you are {age} years old."       
