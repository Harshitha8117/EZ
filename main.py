from fastapi import FastAPI
from routers import auth, upload
from routers import auth, upload, download

app = FastAPI()

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(download.router)

@app.get("/")
def root():
    return {"message": "🚀 FastAPI File Vault with Auth is running!"}
