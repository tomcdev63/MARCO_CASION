import pandas as pd
import sqlite3 as sql
from sqlite3.dbapi2 import Cursor



class SqlManager:


    def __init__(self, DATABASE) -> None:

        self.connection = sql.connect(DATABASE)
        print("Connexion réussie à SQLite")



    def select_dataset(self):

        data_global = pd.read_sql('select Car.Name, Car.Year, OwnerType.Type as Owner_Type, Car.Seats, Motor.Kilometers as Kilometers_Driven, FuelType.Type as Fuel_Type, Transmission.Type as Transmission, Mileage, Motor.Engine, Motor.Power, Car.Price, Car.IsTrain \
                            FROM Car \
                            INNER JOIN Motor on Car.FK_Motor = Motor.Id \
                            INNER JOIN OwnerType on Car.FK_OwnerType = OwnerType.Id \
                            INNER JOIN Transmission on Motor.FK_Transmission = Transmission.Id \
                            INNER JOIN FuelType on Motor.FK_FuelType = FuelType.Id', self.connection)
                            
        print("BDD importée")
        return data_global



    def create_table(self):

        sql_create_predictions_clients = """ CREATE TABLE IF NOT EXISTS predictions_clients (
                                        id integer PRIMARY KEY,
                                        choix_du_modele TEXT NOT NULL,
                                        brands TEXT NOT NULL,
                                        seniority INTEGER NOT NULL,
                                        owner_Type INTEGER NOT NULL,
                                        seats INTEGER NOT NULL,
                                        kilometers_Driven INTEGER NOT NULL,
                                        fuel_Type TEXT NOT NULL,
                                        transmission TEXT NOT NULL,
                                        mileage INTEGER NOT NULL,
                                        engine INTEGER NOT NULL,
                                        power INTEGER NOT NULL,
                                        prediction INTEGER NOT NULL

                                    ); """

        cursor = self.connection.cursor()
        cursor.execute(sql_create_predictions_clients)
        self.connection.commit()

    
    def insert_prediction(self, prediction):

        query = '''INSERT INTO predictions_clients (choix_du_modele, brands, seniority, owner_Type, seats, kilometers_Driven, fuel_Type, transmission, mileage, engine, power, prediction ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        cursor = self.connection.cursor()
        cursor.execute(query, prediction)
        self.connection.commit()
        cursor.close()
        self.connection.close()
        print("Fin de connexion à la BDD SQLite")



            