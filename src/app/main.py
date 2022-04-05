### Pour lancer FastAPI se rendre ds le dossier src : 
# uvicorn main:app --reload

from typing import Optional
from fastapi import FastAPI
from fastapi import responses
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from prediction_api import predictionapi
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles

from bdd_sql_manager import SqlManager

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")

class Predict(BaseModel):

    choix_du_modele:str
    Brands:str
    Seniority:str
    Owner_Type:str
    Seats:str
    Kilometers_Driven:str
    Fuel_Type:str
    Transmission:str
    Mileage:str
    Engine:str
    Power:str


@app.get("/")
def read_root(request: Request):
    
    result = "Type a number"
    # instruction = " Exemple --> http://127.0.0.1:8000/prediction/66.851562/58.088038/1.802132/2.232983/67.020903/80.612872/0.841740/-0.637752"
    return templates.TemplateResponse("form.html", context={"request": request, "result": result})


@app.post("/prediction")
async def predict(request: Request, choix_du_modele: str = Form(...), Brands: str = Form(...), Seniority: str = Form(...), Owner_Type: str = Form(...), Seats: str = Form(...), Kilometers_Driven: str = Form(...), Fuel_Type:str = Form(...), Transmission: str = Form(...), Mileage: str = Form(...), Engine: str = Form(...), Power: str = Form(...)):
    reponse = predictionapi(Brands, Seniority, Owner_Type, Seats, Kilometers_Driven, Fuel_Type, Transmission, Mileage, Engine, Power, choix_du_modele)
    reponse = int(round(reponse[0] * 1000))
    if reponse < 200:
        reponse = 200
    reponse_marco = int(round(reponse + (reponse * 9) / 100))

    DATABASE = r"../../data/data.db"
    sql_manager = SqlManager(DATABASE)
    sql_manager.create_table()
    sql_manager.insert_prediction([choix_du_modele, Brands, Seniority, Owner_Type, Seats, Kilometers_Driven, Fuel_Type, Transmission, Mileage, Engine, Power, reponse])

    if reponse < 2000:
        img = "../static/images/voiture--.jpg"

    elif reponse < 20000:
        img = "../static/images/voiture-+.jpg"

    elif reponse < 50000:
        img = "../static/images/voiture+.jpg"

    else:
        img = "../static/images/voiture++.jpg"

    
    return templates.TemplateResponse("reponse.html", context={"request": request, "result": reponse, "resultmarco": reponse_marco, "img" : img})