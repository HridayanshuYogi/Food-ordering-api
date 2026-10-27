from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Food
from app.schemas import FoodCreate, FoodResponse
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to restaurant"}


@app.get("/menu")
def get_menu():
    return {
        "items": [
            {
                "id": 1,
                "name": "Margherita Pizza",
                "price": 299
            },
            {
                "id": 2,
                "name": "Veg Burger",
                "price": 199
            },
            {
                "id": 3,
                "name": "French Fries",
                "price": 99
            }
        ]
    }

@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {
                "id": 1,
                "customer": "Rahul",
                "item": "Margherita Pizza",
                "quantity": 2,
                "status": "preparing"
            },
            {
                "id": 2,
                "customer": "Ananya",
                "item": "Veg Burger",
                "quantity": 1,
                "status": "delivered"
            }
        ]
    }
@app.post("/foods", response_model=FoodResponse, status_code=201)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    db_food = Food(**food.model_dump())

    db.add(db_food)
    db.commit()
    db.refresh(db_food)

    return db_food


@app.get("/foods")
def get_foods(db: Session = Depends(get_db)):
    foods = db.query(Food).all()
    return foods







# git push -u origin main
# The push means:

#Take the commits that exist in my local Git repository and send them to the remote repository.

#The -u establishes origin/main as the upstream branch, so later you can usually just do:

#git push

#instead of specifying everything again.