from sqlalchemy.orm import Session

from . import models, schemas

def get_user (db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_users(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email= user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_recipes(db: Session, skip: int = 0, limit:int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == id).first()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(link = recipe.link, name = recipe.name, description = recipe.description)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_meals(db: Session, skip: int = 0, limit:int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()


def create_user_meal(db: Session, meal: schemas.MealCreate, user_id: int, recipe_id: int):
    db_meal = models.Meal(**meal.dict(), user_id=user_id, recipe_id = recipe_id)
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal