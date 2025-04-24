from fastapi import FastAPI
from app.routes import router

app = FastAPI(title = "Face Recognition API")
app.include_router(router)