from datetime import datetime, timedelta
from random import uniform, randrange
from pandas import DataFrame
import numpy as np
import sys
import mysql.connector

cnx = mysql.connector.connect(user='root', password='urubu100',
                              host='127.0.0.1', database="project_db")

cursor = cnx.cursor()

def insert_registro(registro):
    cursor.execute("INSERT INTO insert_values(nome, sistema_abastecimento, turbidez, ph, temperatura, coliformes, exec_date) VALUES(%s, %s, %s, %s, %s, %s, %s)", registro)
    cnx.commit()

empresas = [
    'Águas e Esgotos do Piauí',
    'Águas Guariroba',
    'Caesb',
    'CESAMA',
    'Companhia de Água e Esgoto do Amapá',
    'Companhia de Águas e Esgotos do Rio Grande do Norte',
    'Companhia Catarinense de Águas e Saneamento',
    'Companhia de Água e Esgoto do Ceará',
    'Companhia de Água e Esgotos da Paraíba',
    'Companhia de Águas e Esgotos do Estado de Rondônia',
    'Companhia de Gestão dos Recursos Hídricos',
    'Companhia de Saneamento Ambiental do Maranhão',
    'Companhia de Saneamento de Alagoas',
    'Companhia de Saneamento de Minas Gerais',
    'Companhia de Saneamento de Sergipe',
    'Companhia de Saneamento do Pará',
    'Companhia de Saneamento do Paraná',
    'Companhia Espírito Santense de Saneamento',
    'Companhia Estadual de Águas e Esgotos do Rio de Janeiro',
    'Companhia Pernambucana de Saneamento',
    'Companhia Riograndense de Saneamento',
    'Companhia de Saneamento Básico do Estado de São Paulo',
    'Concessionária de Águas e Esgotos de Nova Friburgo',
    'Empresa Baiana de Águas e Saneamento',
    'Empresa Metropolitana de Águas e Energia',
    'Empresa de Saneamento de Mato Grosso do Sul',
    'Prolagos',
    'Saneamento de Goiás',
    'Serviço Autônomo de Saneamento de Pelotas',
    'Sociedade de Abastecimento de Água e Saneamento'
]

sistemas_abastecimento = [
    range(1, 10 + 1),
    range(1, 15 + 1),
    range(1, 12 + 1),
    range(1, 13 + 1),
    range(1, 12 + 1),
    range(1, 15 + 1),
    range(1, 9 + 1),
    range(1, 9 + 1),
    range(1, 7 + 1),
    range(1, 12 + 1),
    range(1, 17 + 1),
    range(1, 16 + 1),
    range(1, 13 + 1),
    range(1, 7 + 1),
    range(1, 2 + 1),
    range(1, 5 + 1),
    range(1, 6 + 1),
    range(1, 12 + 1),
    range(1, 18 + 1),
    range(1, 8 + 1),
    range(1, 6 + 1),
    range(1, 11 + 1),
    range(1, 6 + 1),
    range(1, 15 + 1),
    range(1, 15 + 1),
    range(1, 12 + 1),
    range(1, 14 + 1),
    range(1, 8 + 1),
    range(1, 9 + 1),
    range(1, 15 + 1)
]

def generate_data(months_to_subtract):
    for empresaIndex in range(0, len(empresas)):
        for sistema in sistemas_abastecimento[empresaIndex]:
            turbidez = uniform(0.0, 500.0)
            pH = np.random.normal(7, 1)
            temperatura = uniform(0.0, 60.0)
            coliformes = randrange(0, 1000)
            data_proc = datetime.now() - timedelta(days=30 * months_to_subtract)
            print(f"\nA {empresas[empresaIndex]} teve os seguintes parametros de qualidade no Sistema de Abastecimento de ID {sistema}:")
            print(f"     Turbidez: {turbidez}")
            print(f"     pH: {pH}")
            print(f"     Temperatura: {temperatura}")
            print(f"     Coliformes Termotolerantes por 100 mililitros: {coliformes}")
            print(f"     Data de processamento: {data_proc}")
            insert_registro(( empresas[empresaIndex], sistema, turbidez, pH, temperatura, coliformes, data_proc))

def show_menu():
    print("============================MENU============================")
    print("Para mostrar o menu: MENU")
    print("Para fazer a medição da qualidade da água nas empresas: MEDIR")
    print("Para fazer a medição de meses retroativos: MEDIR <QTD MESES>")
    print("Para consultar os últimos registros de uma empresa ordenado por data: CNSLT <ID EMPRESA>")
    print("Para consultar o último registro de cada empresa ordenado por data: CNSLT")
    print("Para visualizar as empresas afiliadas e seus IDs: EMPRESAS")
    print("Para sair: EXIT")
    print("============================================================")
    receber_input()

def receber_input():
    print("\nO que você gostaria de fazer? ", end='')
    resposta = input()
    resposta_limpa = resposta.split(" ")
    if(resposta_limpa[0] == "MENU"):
        show_menu()
    elif(resposta_limpa[0] == "MEDIR"):
        if(resposta_limpa[-1] == "MEDIR"):
            generate_data(0)
        else:
            for months_to_subtract in range(1, int(resposta_limpa[-1]) + 1):
                print(f"\nDATA: {datetime.now() - timedelta(days=30 * months_to_subtract)}")
                generate_data(months_to_subtract)
    elif(resposta_limpa[0] == "CNSLT"):
        if(resposta_limpa[-1] == "CNSLT"):
            cursor.execute("SELECT nome, turbidez, ph, temperatura, coliformes, exec_date as data FROM insert_values ORDER BY exec_date DESC LIMIT 30")
            df = DataFrame(cursor.fetchall())
            df.columns = cursor.column_names
        else:
            cursor.execute(f"SELECT nome, turbidez, ph, temperatura, coliformes, exec_date as data FROM insert_values WHERE nome = '{empresas[int(resposta_limpa[-1]) - 1]}' ORDER BY exec_date DESC LIMIT 5")
            df = DataFrame(cursor.fetchall())
            df.columns = cursor.column_names

        print(df)
    elif(resposta_limpa[0] == "EMPRESAS"):
        for i in range(1, len(empresas)+1):
            print(f"{i} - {empresas[i-1]}")
    elif(resposta_limpa[0] == "EXIT"):
        print("Até mais!")
        return
    else:
        print("Comando inválido.")

    receber_input()
    
show_menu()