from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import image_routes

app = FastAPI()

# Mount static folder for CSS, JS, uploads, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routes
app.include_router(image_routes.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )