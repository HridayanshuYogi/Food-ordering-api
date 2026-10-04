from fastapi import FastAPI

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






# git push -u origin main
# The push means:

#Take the commits that exist in my local Git repository and send them to the remote repository.

#The -u establishes origin/main as the upstream branch, so later you can usually just do:

#git push

#instead of specifying everything again.