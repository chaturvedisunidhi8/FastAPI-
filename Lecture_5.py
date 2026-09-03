from fastapi import FastAPI
from MockData import products
from dtos import ProductDTO
app=FastAPI()  #object

#Different types of HTTP requests
#@app.post("/create_products")
#def create_products(product_data:ProductDTO):  #data is the object of ProductDTO class
#    print(product_data)  #this will print the data in the console
#    return {
#        "message": "Product Created Successfully"
#    }

''' to get data in dictionary in console'''

@app.post("/create_products")
def create_products(product_data:ProductDTO):  #data is the object of ProductDTO class
    product_data=product_data.model_dump()  #this will convert the data into dictionary
    print(product_data)  #this will print the data in the console
    products.append(product_data)



    return {
        "message": "Product Created Successfully","data":products 
    }

#now send again in postman and you will get output as Product Created Successfully and in console you will get the data which you sent in postman in dictionary format
#now how can i store this data in my backend so write now we are not using practical DBs like mysql,postgresql etc so we will use mock data to store the data in backend and we will use list to store the data in backend
#here we are storing this data in our memory so for that

#products.append(product_data)  #this will append the data in the list after doing this again send request from postman
#after doing this you can the 3rd item on console of postman, now you can check with different different data on postman





#Methods to send data
# 1) Method:body:  - we can send data in body of request, and we can use postman to send data in body of request
# 2)Headers and we call request headers
# 3)Queries params 



#1) we are learning BODY choose Raw and JSON -
#we just send data using BODY but now the question is how do we get that data in our server  
#now data will come inside body but how fastapi get to know that this data is post data means it came to body by POST method just by writing body in function i cant figure out this
#So here pydantic came into picture -- it is used for data validation and settings management using python type annotations. It is used to define the structure of the data that we expect to receive in the request body. By creating a Pydantic model, we can specify the fields and their types, and FastAPI will automatically validate the incoming data against this model.
#lets create a DTOS file (Read learn>>tutorials guide>>request body part of fastapi doc)so there you will find
#A request body is data sent by the client to your API. A response body is the data your API sends to the client.
#so these are possible ways through which we can send data to server 
#after making changes in dtos file when you will send data in postman you will get output as Product Created Successfully and in console you will get the data which you sent in postman




#How to call different HTTP methods:   - any tool

#Note:for our POST method,client send data to server so here,we have postman as client and our project is working as a server


#How to validate data in a request  - It is known as DTOS (data transfer objects)

#pydantic validates data if in postman we give a data in post by missing any of the required field(which doesnt have default value) then it will give us error message in postman and in console it will print the data which we sent in postman
#so it will give an error 





#"""hello """
#print(__doc__)


#Path Parameters
@app.get("/products/{products_id}")                # input http://127.0.0.1:8000/products/1
def get_products(products_id:int):                 # output will be product with id 1
    return {
        "id":products_id,
    }


#PUT METHOD
@app.put("/update_products/{products_id}")          #for path parameter or if you want then you can also use query parameter
def update_product(product_data:ProductDTO,products_id:int):
    #now we will update the productso we will apply a for loop
    for index, oneProduct in enumerate(products):
        if oneProduct["id"] == products_id:
            products[index] = product_data.model_dump()  #this will convert the data into dictionary
            return {
                    "status": "Product Updated Successfully","product":products[index]
                }


    return {
        "status": "Product not found with this ID",
    }



#delete method
@app.delete("/delete_products/{products_id}")
def delete_product(products_id:int):
     for index, oneProduct in enumerate(products):
         if oneProduct["id"] == products_id:
             deleted_product=products.pop(index)  #this will remove the product from the list and return the deleted productreturn {
             return{"status": "Product Deleted Successfully","deleted_product":deleted_product}
     return {
        "status": "Product not found with this ID",
    }
         