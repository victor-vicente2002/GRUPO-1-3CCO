from datetime import datetime
import tracemalloc

def algas(bank_transaciton):
    tracemalloc.start()
    
    dt_inicio = datetime.now()
    dt_fim = 0
    accumulate= 0
    
    for i in range(1, bank_transaciton+1):
        accumulate += i
    dt_fim = datetime.now()

    time_elapsed = dt_fim - dt_inicio

    tracemalloc.stop()


def menu():
    print('''
            MENU:

            [1] - Range A: 100000, 600000, 100000
            [2] - Range B: 1000, 6000, 100
            [3] - Range C: 100, 600, 100
            [4] - Range D: 10, 60, 10
            [5] - Range E: 1000000, 6000000, 1000000
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
    
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        system.exit(0)

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(2):

    valores = []
    valores = []
    for valor in range(1000, 6000, 100):
        algasDados = algas(valor)
   
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        system.exit(0)

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")
       

if(3):

    valores = []
    for valor in range(100, 600, 100):
     algasDados = algas(valor)
   
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        system.exit(0)

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")
       

if(4):

    valores = []
    for valor in range(10, 60, 10):
        algasDados = algas(valor)
    
    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        system.exit(0)

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(5):

    valores = []
    for valor in range(1000000, 6000000, 1000000):
     algasDados = algas(valor)

    print("Deseja fazer outra interação?")
    interacao = input('Digite somente \n S - SIM \n N - NÃO \n')
    
    if(interacao == "S"):
        print("Voltando ao menu...") 
        menu()

    elif(interacao == "N"):
        print("Obrigada!")
        system.exit(0)

    else:
        print("Digite somente \n S - SIM \n N - NÃO ")


if(6):
    print("Conexao encerrada")
