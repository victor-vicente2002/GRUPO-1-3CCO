from operator import imod
import psycopg2
import time
import tracemalloc
import sys
from datetime import timedelta, datetime

blocks = [
    range(100_000, 600_000, 100_000),
    range(1_000, 6_000, 100),
    range(100, 600, 100),
    range(10, 60, 10),
    range(1_000_000, 6_000_000, 1_000_000)
]

numBlock = 0
dataTransaction = []
        
def sum_of_init(transaction):
    # mv = memoryview(b'accumulate')
    dt_inicio = time.time()
    tracemalloc.start()
    accumulate = 0

    for i in range(1, transaction +1):
        accumulate += i

    dt_fim = time.time()
    memory = tracemalloc.get_traced_memory()[1]
    dataTransaction.append({'i': i, 'block_transaction': numBlock,'transactions': transaction, 'accumulate': accumulate, 'memory': memory, 'time_elapsed': (dt_fim - dt_inicio)})
    tracemalloc.stop()


def connectAndInsert(insertedValues):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
          host="localhost",
          database="measures",
          user="postgres",
          password="senha123",
          port="3306")
        # create a cursor
        cur = conn.cursor()
        for i in insertedValues:
	      # execute a statement
            postgres_insert_query = """ INSERT INTO measures (block_transaction, transactions, accumulate, memory, time_elapsed) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (i['block_transaction'], i['transactions'], i['accumulate'], i['memory'], i['time_elapsed'])
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
        print(f'Erro: {error}')
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


for bank_transactions in blocks:
    numBlock += 1
    for transaction in bank_transactions:
        sum_of_init(transaction)
        
connectAndInsert(dataTransaction)
