import psycopg2
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def gen_data(n):
    tracemalloc.start()

    dt_start = datetime.now()
    acc = 0

    for i in range(1, n + 1):
        acc += i
    dt_end = datetime.now()

    rtn = (n, acc, tracemalloc.get_traced_memory()[1], (dt_end - dt_start).total_seconds())
    tracemalloc.stop()
    return rtn

def connect():
    return psycopg2.connect(host="localhost", port=5432, database="measures", user="postgres", password="docker")

def disconnect(cur, conn):
    cur.close()
    conn.close()

def insert(value, acc, used_memory, time_elapsed):
    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO measures(value, acc, used_memory, time_elapsed) VALUES(%s, %s, %s, %s)",
                (value, acc, used_memory, time_elapsed))
    conn.commit()

    disconnect(cur, conn)

def find_all():
    conn = connect()
    cur = conn.cursor() 

    cur.execute("""SELECT * FROM measures""")
    query_results = cur.fetchall()
    print(query_results)

    disconnect(cur, conn)

res = []
for value in range(1000, 100000, 1000):
    res.append(gen_data(value))

for value in res:
    print(value)
    insert(value[0], value[1], value[2], value[3])
# find_all()

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()