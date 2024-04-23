# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:01:59 2024

@author: joan camilo tamayo

pip install snowflake-connector-python

"""
import pandas as pd
import snowflake.connector
from config import account, user, password, warehouse, database, schema, table, role

# Conéctate a Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema,
    role=role 
)

# elimino variables privadas 
del account, user, password, role

# Crea un cursor para ejecutar consultas SQL
cur = conn.cursor()

# Ejecuta una consulta para seleccionar todos los datos de la tabla
query = f"SELECT * FROM {table}"
cur.execute(query)

# Recupera los resultados
results = cur.fetchall()

# Cierra el cursor y la conexión
cur.close()
conn.close()

#  nombres de las columnas
columns = [col[0] for col in cur.description]


df = pd.DataFrame(results, columns=columns)
df_muestra = df.head(100)


