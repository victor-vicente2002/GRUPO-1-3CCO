from contextlib import nullcontext
import random 

valores = 0
while valores < 100:

    valores += 1

    for dadosReais in range(1):

        dadosnivel = random.uniform(0.0 , 10.0 * 1)
        dadosnivel = round(dadosnivel, 2)

    dadosfake = dadosnivel 

    if(valores == 12 ):
         dadosnivel = "null"

    if(valores == 25 ):
        dadosnivel = "null"
        
    if valores == 100:
        break
    

    print("ID:",valores, ", Nivel da agua:",dadosnivel )
else:
    print("fim while")


       



