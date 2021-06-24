from sqlalchemy import create_engine
# import psycopg2
# import logging
import threading
import time
# from datetime import datetime

db_credential_sqlserver = {
    "provider" : "mssql+pyodbc",
    "user" : "SA",
    "password" : "Claveomia1*",
    "host" : "107.20.91.241",
    "port" : "1433",
    "database" : "Omia",
    "driver" : "/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1"
}

# engine = create_engine('postgresql://digevo:Digevobd*@database-omia.ccco8vwbpupr.us-west-2.rds.amazonaws.com:5432/postgres')

engine = create_engine("{}://{}:{}@{}:{}/{}?driver={}".format(*db_credential_sqlserver.values()))

# print('postgresql://{}:{}@{}:{}/{}'.format(*credentials.values()))

query = 'select * from alerta_alarmas where id_alarma in (select max(id_alarma) as id_alarm from alerta_alarmas group by camara_id)'

# # where id_alarma in (select max(id_alarma) as id_alarm from alerta_alarmas group by camara_id)
result = engine.execute(query)

for _r in result:
   print(_r)