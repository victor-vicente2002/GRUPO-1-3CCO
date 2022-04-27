from datetime import datetime, timedelta
# import matplotlib.pyplot as plt
import numpy as np
import tracemalloc
import mysql.connector as mysql
from mysql.connector import Error
connection = None

blocks = [
    range(100_000, 600_000, 100_000),
    range(1_000, 6_000, 100),
    range(100, 600, 100),
    range(1_000_000, 6_000_000, 1_000_000)
]

def soma_tempo(n):
    tracemalloc.start()
    
    dt_inicio = datetime.now()
    end_date = 0
    accumulator = 0
    
    
    for i in range(1, n+1):
        accumulator += i
    end_date = datetime.now()
    memory = tracemalloc.get_traced_memory()[1] # segundo elemento representa o pico da memoria
    time = (end_date - dt_inicio).microseconds
    retorno = { 
        'bank_transaction': n, 
        'accumulate': accumulator,
        'memory': memory,
        'time_elapsed': time,
    }
    tracemalloc.stop()
    tracemalloc.clear_traces()
    return retorno

def save_block(index):
    try:
        connection = mysql.connect(
            host = 'localhost',
            database = 'measures',
            user = 'root',
            password = 'algas123'
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()

            valores = []
            block = blocks[index]
            for valor in block:
                current = soma_tempo(valor)
                date = datetime.now() #- timedelta(days= days)
                query = "insert into transactions(bank_transaction, accumulate, memory, time_elapsed, exec_date, block_transaction) values (%s, %s, %s, %s, %s, %s);"
                query_data = (current['bank_transaction'], current['accumulate'], current['memory'], current['time_elapsed'], date, index)
                print(query_data)
                cursor.execute(query, query_data)
                connection.commit()
                print("ok")
                valores.append(current)

            # plt.plot(
            #     np.array([item['time_elapsed'] for item in valores]),
            #     np.array([item['memory'] for item in valores]),
            # )
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection != None and connection.is_connected():
            cursor.close()
            connection.close()
        print("MySQL connection is closed")

option = 0
while option != 5:
    print("Leitura da quantidade de sólidos dissolvidos na água.")
    print("Selecione a estação do ano")
    option = int(input("\t1. Verão\n\t2. Inverno\n\t3. Outono\n\t4. primavera\n\t5. Sair\n> "))
    if option == 1:
        save_block(0)
    elif option == 2:
        save_block(1)
    elif option == 3:
        save_block(2)
    elif option == 4:
        save_block(3)
    elif option == 5:
        print("Até mais!")
    else:
        print("Por favor, digite uma opção válida")
