from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola desde FastAPI en Render!"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Carlos"}
    ]

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)