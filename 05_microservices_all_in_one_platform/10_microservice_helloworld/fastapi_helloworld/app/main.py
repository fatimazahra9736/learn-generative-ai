from fastapi import FastAPI

app = FastAPI(title="Hello World API" , 
              version= "0.0.1" ,
              servers=[
                  {
                    "url" : "http://0.0.0.0:8000",
                    "description" : "Development server"
                  }
              ]
            )

@app.get("/")
def read_root():
    return {"hello" : "world"}

