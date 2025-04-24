# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from services.bg_remover import remove_background
from io import BytesIO

app = FastAPI(title="Background Remover API")

@app.get("/")
def read_root():
    return {"message": "Upload an image to remove its background"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        result_bytes = remove_background(file)
        return StreamingResponse(BytesIO(result_bytes), media_type="image/webp")
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import subprocess
    subprocess.run(["gunicorn","main:app","--workers","4","--worker-class","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000","--reload"])