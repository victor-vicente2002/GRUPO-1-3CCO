from operator import imod
import psycopg2
import time
import tracemalloc
import sys

def sum_of_init(n):
    tracemalloc.start()
    dt_inicio = time.time()
    state = []
    accumulate = 0
    for i in range(1, n+1):
        accumulate += i
    # mv = memoryview(b'accumulate')
    dt_fim = time.time()
    state.append({'i': i, 'accumulate': accumulate, 'memory': sys.getsizeof(accumulate), 'time': (dt_fim - dt_inicio)})
    tracemalloc.stop()
    print(state)
    return state


def connectAndInsert(insertedValues):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
          host="localhost",
          database="velocimetro",
          user="postgres",
          password="senha123",
          port="3306")
        # create a cursor
        cur = conn.cursor()
        for i in insertedValues:
	      # execute a statement
            postgres_insert_query = """ INSERT INTO insert_values (accumulate, memory, time) VALUES (%s,%s,%s)"""
            record_to_insert = (i['accumulate'], i['memory'], i['time'])
            print('PostgreSQL database version:')
            cur.execute(postgres_insert_query, record_to_insert)
            conn.commit()
            count = cur.rowcount
            print(count, "Record inserted successfully into mobile table")
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# for valor in [100000, 2000000, 9000000, 7500000, 1000000, 24449, 9760978, 10, 78, 1325769]:
#     # iteracoes = sum_of_init(valor)
#     connectAndInsert(sum_of_init(valor))

for valor in range(1, 10 ** 5):
    sum_of_init(valor)