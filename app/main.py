from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to restaurant"}


@app.get("/menu")
def get_menu():
    return {
        "items": [
            {"id": 1, "name": "Pizza", "price": 250},
            {"id": 2, "name": "Burger", "price": 150},
            {"id": 3, "name": "Biryani", "price": 200}
        ]
    }