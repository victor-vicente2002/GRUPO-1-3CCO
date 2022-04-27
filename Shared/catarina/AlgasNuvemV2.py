from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import tracemalloc
import mysql.connector
con = mysql.connector.connect(host='localhost',database='ALGASCATARINA',user='root',password='temp123')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)


def algas(agua_intervalo):
    tracemalloc.start()
    
    dt_inicio = datetime.now()
    dt_fim = 0
    accumulate= 0
    
    for i in range(1, agua_intervalo+1):
        accumulate += i
    dt_fim = datetime.now()

    ph = dt_fim - dt_inicio

    
    dadosReturn = f" {agua_intervalo},{accumulate},{tracemalloc.get_traced_memory()[1] / 10},{ph.total_seconds()} "

    tracemalloc.stop()

    return dadosReturn


def insertDados(paramentosData):
     
    mycursor = con.cursor()

    mycursor.execute(f'''INSERT INTO inset_values (agua_intervalo, accumulate, memory, ph) 
    VALUES ({paramentosData})''')

    con.commit()


def menu():
    print('''
            Qual a quantidade Litros de água você deseja liberar?

            MENU:

            [1] - Range A: 100000L a 600000L em 100000L
            [2] - Range B: 1000L a 6000L em 100L
            [3] - Range C: 100L a 600L em 100l
            [4] - Range D: 10L a 60L em 10L
            [5] - Range E: 1000000L a 6000000L em 1000000L
            [6] - Sair

        ''')
    str(input('Escolha uma opção: '))

RangeA = "1"
RangeB = "2"
RangeC = "3"
RangeD = "4"
RangeE = "5"
sair = "6"


menu()

if(1):

    valores = []
    for valor in range(100000, 600000, 100000):
        algasDados = algas(valor)
        valores.append(algasDados)
        insertDados(algasDados)
    
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        print(algasDados)
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        exit()

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(2):

    valores = []
    valores = []
    for valor in range(1000, 6000, 100):
        algasDados = algas(valor)
        valores.append(algasDados)
        insertDados(algasDados)
   
   
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        exit()

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")
       

if(3):

    valores = []
    for valor in range(100, 600, 100):
        algasDados = algas(valor)
        valores.append(algasDados)
        insertDados(algasDados)
   
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        exit()

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")
       

if(4):

    valores = []
    for valor in range(10, 60, 10):
        algasDados = algas(valor)
        valores.append(algasDados)
        insertDados(algasDados)
    
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        exit()

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(5):

    valores = []
    for valor in range(1000000, 6000000, 1000000):
        algasDados = algas(valor)
        valores.append(algasDados)
        insertDados(algasDados)

    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        exit()

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(6):
    print("Conexao encerrada")
