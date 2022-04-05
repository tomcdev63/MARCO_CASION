import pickle
import pandas as pd

def predictionapi(Brands, Seniority, Owner_Type, Seats, Kilometers_Driven,Fuel_Type, Transmission, Mileage, Engine, Power, choix_du_modele):

    '''
    Renvoi prediction

    '''

    Seniority = int(Seniority)
    Seats = int(Seats)
    Kilometers_Driven = int(Kilometers_Driven)
    Owner_Type = int(Owner_Type)
    Mileage = int(Mileage)
    Engine = int(Engine)
    Power = int(Power)

    cols = ["Brands", "Seniority", "Owner_Type", "Seats", "Kilometers_Driven", "Fuel_Type", "Transmission", "Mileage", "Engine", "Power"]

    model = pickle.load(open("../../data/models/"+ choix_du_modele,"rb"))
    preprocessor = pickle.load(open("../../data/preprocessor/preprocessor2","rb"))

    liste_arg = [Brands, Seniority, Owner_Type, Seats, Kilometers_Driven,Fuel_Type, Transmission, Mileage, Engine, Power]
    print(liste_arg)
    rows_df = pd.DataFrame([liste_arg], columns=cols)
    preprocessed_row = preprocessor.transform(rows_df)
    estimation = model.predict(preprocessed_row)
    
    print (f"Estimation du bien : {choix_du_modele}, {estimation} euros.")
    return estimation



