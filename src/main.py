import uvicorn

from fastapi import FastAPI

app = FastAPI(
        title="Finmate API", 
        description="An assistant for financial planning and management"
        )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Finmate API!"}

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="localhost", 
        port=8000,
        log_level="info",
        reload=True,
        worker_class="uvicorn.workers.UvicornWorker",
        workers=4
        )