#Lecture -4 
from fastapi import FastAPI ,Request
from MockData import products

app=FastAPI()  #object

#2
@app.get("/products")
def get_products():
    return products




#Path Parameters
#@app.get("/products/{products_id}")                # input http://127.0.0.1:8000/products/1
#def get_products(products_id:int):                 # output will be product with id 1
#    return {
#        "id":products_id,
#    }






### Path Params
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
#    }                                                   #output --- {"id":1,"name":"Laptop","price":50000,"count":5}

#@app.get("/greet")
#def greet_user():
#    return "Hello User, Welcome to FastAPI"






#@app.get("/greet")
#def greet_user(name:str,age:int):                                    #suppose we want to greet user with his name, then we can use query params
#    return {  
#        "greet": f"Hello {name},and you are {age} years old."        #now whatever we will pass in path like http://127.0.0.1:8000/greet?name=John we will get output as Hello John, Welcome to FastAPI
#    }
#
#def greet_user(name:str,age:int):   #this is fine but what if we get 300 data then 





@app.get("/greet")
def greet_user(request:Request):   #this is fine but what if we get 300 data then     
         #print(request.query_params)        #input --- http://127.0.0.1:8000/greet?name=Sunidhi&age=22    ,  
         #output --- {"greet":"Hello ,and you are years old."}
        query_params=dict(request.query_params)  #this will give us all the query params in the form of dictionary  
        print(query_params)
        return {
             "greet": f"Hello {query_params.get('name')}  ,You are {query_params.get('age')} years old."     
        }




                                                           

#Request has all details like query parameter, body parameters,path parameter ,IP address 
# so how will you get the request in above function ,we write request in above function but here fastapi dont knwo what is request ,so we will import request from request
#so response has all the details of the request and we can get the query parameters from the request object using request.query_params
#but here we want query_params so we will write request.query_params and it will give us the query parameters in the form of dictionary
