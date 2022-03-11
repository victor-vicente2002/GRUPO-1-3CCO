#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector
con = mysql.connector.connect(host='localhost',database='catarina',user='aluno',password='sptech')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
#if con.is_connected():
#    cursor.close()
#    con.close()
#    print("Conexão ao MySQL foi encerrada")


# In[9]:


cursor = con.cursor()
sql = "INSERT INTO dados (memoria, tempo) VALUES (%s, %s)"
values = (70, 30)
cursor.execute(sql, values)


print(cursor.rowcount, "record inserted.")
print("\n")

sql = ("SELECT id, memoria, tempo FROM dados")
cursor.execute(sql)


# In[ ]:




