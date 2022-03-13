from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import tracemalloc
import mysql.connector
con = mysql.connector.connect(host='localhost',database='ALGASCATARINA',user='root',password='root')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)


def algas(bank_transaciton):
    tracemalloc.start()
    
    dt_inicio = datetime.now()
    dt_fim = 0
    accumulate= 0
    
    for i in range(1, bank_transaciton+1):
        accumulate += i
    dt_fim = datetime.now()

    time_elapsed = dt_fim - dt_inicio

    
    dadosReturn = f" {bank_transaciton},{accumulate},{tracemalloc.get_traced_memory()[1] / 10},{time_elapsed.total_seconds()} "

    tracemalloc.stop()

    return dadosReturn


def insertDados(paramentosData):
     
    mycursor = con.cursor()

    mycursor.execute(f'''INSERT INTO insert_values (bank_transaciton, accumulate, memory, time_elapsed) 
    VALUES ({paramentosData})''')

    con.commit()


# a)
valores = []
for valor in range(100000, 600000, 100000):
    algasDados = algas(valor)
    valores.append(algasDados)
    insertDados(algasDados)

# b)
    valores = []
for valor in range(1000, 6000, 100):
    algasDados = algas(valor)
    valores.append(algasDados)
    insertDados(algasDados)
    

# c)
    valores = []
for valor in range(100, 600, 100):
    algasDados = algas(valor)
    valores.append(algasDados)
    insertDados(algasDados)


# d)
    valores = []
for valor in range(10, 60, 10):
    algasDados = algas(valor)
    valores.append(algasDados)
    insertDados(algasDados)
    

# e)
    valores = []
for valor in range(1000000, 6000000, 1000000):
    algasDados = algas(valor)
    valores.append(algasDados)
    insertDados(algasDados)

cursor.close()
con.close()
print("Conexao encerrada ",linha)