import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, the server is alive"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8500)






