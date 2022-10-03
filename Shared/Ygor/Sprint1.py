import json
import datetime
import random
import numpy as np
import time
TEMPO_ESPERA = 10 # 10 Segundos


def gerarCondutividade():
    # 10% de chance de não gerar informação
    if round(random.uniform(0, 10)) == 7:
        return 'NULL'

    # 1% de chance de dar uma amostra "estranha"
    if round(random.uniform(0, 100)) == 7:
        return random.uniform(0.7, 50000)


    return np.random.normal(200, 5, size=1)[0]

while True:
    data = {
        "condutividade": gerarCondutividade(),
        "dataHora": str(datetime.datetime.now())
    }

    print("Coletando informações de condutividade")
    print(data)

    time.sleep(TEMPO_ESPERA)