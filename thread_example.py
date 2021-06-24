from sqlalchemy import create_engine
import psycopg2
# import logging
import threading
import time
from datetime import datetime
# psycopg2
engine = create_engine('postgresql://digevo:Digevobd*@database-omia.ccco8vwbpupr.us-west-2.rds.amazonaws.com:5432/postgres')


# result = engine.execute('select * from public.dev_fast order by rd_id desc limit 2')

# engine.execute("insert into public.dev_fast(camara_id,obj_type,analytic_id,inst_analytic_id,total,timestamp,session_id) values ('440', '1', '2', '2', '0', '2021-05-12 12:53:11', '2021-05-12 12:52:58')")

# result = engine.execute('select * from public.fast_analytics limit 10')

# for _r in result:
#    print(_r)
# total = 
# timestamp =

def getTimestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def creathread(valor):
    x = threading.Thread(target=inserta, args=(valor,))
    x.start()
#    time.sleep(.1)

def inserta(valor):
    print('insertando', valor)
    #   time.sleep(1)
    engine.execute(valor)
    print('acaba insertar', valor)

def main():
    print('inicio')

    session_id = getTimestamp()

    for ii in range(30):
    #   print(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        creathread("insert into public.dev_fast(camara_id,obj_type,analytic_id,inst_analytic_id,total,timestamp,session_id) values ('440', '1', '2', '2', '{}', '{}', '{}')".format(str(ii),getTimestamp(),session_id)) #pasar el string a insertar

if __name__ == "__main__":
    main()