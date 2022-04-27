import psycopg2
import tracemalloc
# import matplotlib.pyplot as plt
# import numpy as np
from datetime import datetime, timedelta

blocks = [
    range(100_000, 600_000, 100_000),
    range(1_000, 6_000, 100),
    range(100, 600, 100),
    range(10, 60, 10),
    range(1_000_000, 6_000_000, 1_000_000)
]

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
    return psycopg2.connect(host="localhost", port=5432, database="water_measures", user="postgres", password="postgres")

def disconnect(cur, conn):
    cur.close()
    conn.close()

def insert(value, acc, used_memory, time_elapsed):
    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO water_measures(sample_score, sulfates, sample_qty, chloramines) VALUES(%s, %s, %s, %s)",
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

for block in blocks:
    print("\n", "executing block", block)
    executions = []
    for transaction in block:
        executions.append(gen_data(transaction))
    for execution in executions:
        print(execution)
        insert(execution[0], execution[1], execution[2], execution[3])

# for value in range(1000, 100000, 1000):
#     res.append(gen_data(value))

# for value in res:
#     print(value)
#     insert(value[0], value[1], value[2], value[3])
# find_all()

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()