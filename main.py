import uvicorn
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))


if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
