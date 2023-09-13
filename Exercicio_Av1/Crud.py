from pymongo import MongoClient
import datetime
class Database:
    def __init__(self,database):
        self.database = database

    def inserir_info(self,nomeSensor:str, valorSensor:int, alarmado:bool):
        try:
            response = self.database.insert_one({
                                    "NomeSensor": nomeSensor,
                                    "valorSensor": valorSensor,
                                    "Alarmado": alarmado,
                                    "horario": datetime.datetime.now(),
                                })
            return response.inserted_id
        except Exception as e:
            print("Ocorreu um erro ao inserir: ",e)
            return None

    def update_info(self,nomeSensor:str, valorSensor:int, alarmado:bool):
        try:
            response = self.database.update_one({"NomeSensor": nomeSensor}, {"$set": {"valoSensor": valorSensor, "alarmado": alarmado,"horario":datetime.datetime.now()}})
            return None
        except Exception as e:
            print("Ocorreu um erro ao inserir: ",e)
            return None

    def read_info(self,nomeSensor:str):
        try:
            response = self.database.find_one({"NomeSensor": nomeSensor}, {"alarmado":1})
            return response
        except Exception as e:
            print("Ocorreu um erro ao inserir: ",e)
            return None
