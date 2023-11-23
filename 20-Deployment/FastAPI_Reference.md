# FastAPI Reference
To begin using FastAPI, the first step is to install the required libraries, namely FastAPI itself and Unicorn. You can achieve this by using the following pip command:

    pip install fastapi uvicorn pydantic

It's important to note that the number of libraries you install depends on the specific requirements of your project, and there may be additional dependencies beyond these two.

----------
## Getting Started!


1. **Setting Up Your Project**

Start by creating a new folder for your project. Within this folder, create a file named `**main.py**`. This file will contain the initial FastAPI code.

----------
2. **Writing Your First FastAPI Code**

In the `**main.py**` file, add the following code:


    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    def root():
      return "Welcome To Tuwaiq Academy"

This simple FastAPI application creates an instance of the FastAPI class and defines a single route ("/") that returns a welcome message.

----------
3. **Running Your FastAPI Server Locally**

To run your FastAPI server locally, open your command line and enter the following command:


    uvicorn main:app --reload

The `**main**` refers to the name of your Python file (`**main.py**`), and `**app**` is the name of the FastAPI instance in your code. The `**--reload**` flag enables automatic reloading of the server when changes are made to the code.


- `**--host**` **and** `**--port**`:
    - Specify the host and port on which your FastAPI server will run. For example:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    - This command runs the server on all available network interfaces (`**0.0.0.0**`) and sets the port to `**8000**`.
    
- `**--workers**`:
    - Configure the number of worker processes to handle incoming requests. For example:
    uvicorn main:app --reload --workers 4
    - This command starts the server with 4 worker processes. The number can be adjusted based on your server's requirements and available resources.
    
- `**--log-level**`:
    - Set the log level for the server. Options include `**critical**`, `**error**`, `**warning**`, `**info**`, and `**debug**`. For example:
    uvicorn main:app --reload --log-level debug
    - This command sets the log level to `**debug**`, providing more detailed logs for debugging purposes.
----------
4. **Accessing Your FastAPI Application**

Open your web browser and navigate to the following URL:

- `**http://127.0.0.1:8000**` or `**http://localhost:8000**`

You should see your FastAPI application's welcome message displayed in the browser. This confirms that your FastAPI server is up and running locally.

**Interactive Documentation:**
FastAPI generates interactive documentation automatically, which can be accessed at `**/docs**` and `**/redoc**`:

- **Swagger UI (**`**/docs**`**)**:
    - Visit `**http://127.0.0.1:8000/docs**` or `**http://localhost:8000/docs**` in your browser.
    - You'll see an interactive UI where you can explore your API, send requests, and view responses.
    - The interactive documentation is generated based on the types and comments in your code.
![](https://paper-attachments.dropboxusercontent.com/s_C2C3C6BF9E4A0E4C55E730CAEC344CD08ECEF5E30F9F9CEC23B4FFE6A367F970_1699970497399_Screenshot+1445-04-30+at+5.00.48PM.png)

----------

**Defining Different HTTP Methods:**
FastAPI makes it simple to create API endpoints with various HTTP methods. Let's extend the example by adding a POST endpoint for creating a new item and a PUT endpoint for updating an existing item.

    from fastapi import FastAPI, HTTPException
    
    app = FastAPI()
    
    # GET request
    @app.get("/")
    def read_root():
        return {"message": "Welcome to Tuwaiq Academy"}
    
    # POST request
    @app.post("/items/")
    def create_item(item: dict):
        return {"item": item}
    
    # PUT request
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: dict):
        return {"item_id": item_id, "updated_item": item}

In this example:

- The `**create_item**` endpoint accepts a POST request with a JSON payload representing an item.
- The `**update_item**` endpoint accepts a PUT request with a path parameter (`**item_id**`) and a JSON payload representing the updated item.


----------

**Handling HTTPExceptions:**
To handle errors and exceptions, you can use the `**HTTPException**` class provided by FastAPI. For example:

    from fastapi import HTTPException
    
    # GET request with exception handling
    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        if item_id == 42:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"item_id": item_id}
    

In this example, if the requested `**item_id**` is 42, it raises a 404 HTTPException with a detailed message.

----------

These are just basic examples to get you started. FastAPI offers a wide range of features for handling request validation, authentication, dependencies, and more. As you build more complex APIs, you can explore these features to create robust and secure applications. Always refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) for detailed information and examples.



