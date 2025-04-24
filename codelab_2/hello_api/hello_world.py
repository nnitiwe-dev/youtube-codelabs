from fastapi import FastAPI 

# Create an instance of FastAPI 
app = FastAPI() 

# Define a root route ("/") 
@app.get("/") 
async def root(): 
      return {"message": "Hello, World!"}

if __name__ == "__main__":
    import subprocess
    subprocess.run(["gunicorn","hello_world:app","--workers","4","--worker-class","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000","--reload"])