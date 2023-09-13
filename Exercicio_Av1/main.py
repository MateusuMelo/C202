import random
import threading
import time
from Crud import Database
from pymongo import MongoClient

def gen_value(nome, intervalo):
    exists = False
    while True:
        value = random.randrange(30,40)
        alarmado = False
        try:
            client = MongoClient('mongodb://localhost:27017')
            db = client['Bancoiot']
            sensores = db.sensores
            data = Database(sensores)
        except Exception as e:
            print(e)

        print(nome,value)

        try:
            flag = data.read_info(nome)['alarmado']
            if bool(flag) == True:
                time.sleep(intervalo)
                break
        except Exception as e:
            print(e)

        if value > 38:
            alarmado = True
            print("Atencao! Temperatura muito alta! verificar sensor ",nome)
            data.update_info(nome, value, alarmado)


        if exists == False:
            data.inserir_info(nome, value, alarmado)

        data.update_info(nome,value,alarmado)
        time.sleep(intervalo)


        exists = True


Temp1 = threading.Thread(target=gen_value, args=("Temp1",1))
Temp2 = threading.Thread(target=gen_value, args=("Temp2",1))
Temp3 = threading.Thread(target=gen_value, args=("Temp3",1))

while True:
    Temp1.start()
    Temp2.start()
    Temp3.start()