import pyodbc
import pandas as pd
import datetime
import json
import time


# lista todas las cam_id asignadas a los malls
#json no acepta int64 asique se tarbaja en str
m1=set([str(x) for x in range (76,86)])
m2=set([str(x) for x in range (11,21)])
m3=set([str(x) for x in range (21,31)])
m4=set([str(x) for x in range (31,41)])
m5=set([str(x) for x in range (41,51)])
m6=set([str(x) for x in range (51,61)])
m7=set([str(x) for x in range (61,71)])
m8=set([str(x) for x in range (71,81)])

malls_dic = {'Mall 1':m1,'Mall 2':m2,'Mall 3':m3,'Mall 4':m4,'Mall 5':m5,'Mall 6':m6,'Mall 7':m7,'Mall 8':m8}

no_result = {'Mall 1':[], 'Mall 2':[], 'Mall 3':[], 'Mall 4':[], 'Mall 5':[], 'Mall 6':[] ,'Mall 7':[],'Mall 8':[]}

server = '107.20.91.241,1433'
database = 'Omia'
username = 'SA'
password = 'Claveomia1*'
cnxn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#query = pd.read_sql_query(
#      '''select top 1000 * from dbo.alerta_alarmas where fecha_alarma >= dateadd(minute, -1, getdate()) and fecha_alarma <= dateadd(minute, 1, getdate()) order by fecha_alarma desc''', cnxn)
""" query = pd.read_sql_query(cle
            'select top 1000 * from dbo.alerta_alarmas order by fecha_alarma desc', cnxn) """

query = None

def read_table_alarmas():
    query = pd.read_sql_query(
                'select * from alerta_alarmas where id_alarma in (select max(id_alarma) as id_alarm from alerta_alarmas group by camara_id)', cnxn)


    query['camara_id'] = query['camara_id'].astype(str) #json no acepta el int64 asique se genera en str
    return query


#obtenemos id mall y camaras con alarma del modo {1:'0',...'5'} donde solo estan los que existen
def get_mall_cams_alerts(df, malls = malls_dic):
    result = dict()
    #new_alerts = checkTime(df)
    # print(df)
    # obtenemos solo los cam id distintos en el objeto diff_ids
    diff_ids = set(df[df['is_alarm'] == 1].camara_id.unique())
    for id_mall, cam_ids in malls.items():
        common_cam_ids = cam_ids.intersection(diff_ids)
        ids = list(common_cam_ids)
        result[id_mall] = ids
    #result = list(df.camara_id)
    # print('Results v5: ', result)
    return result

def retrieve():
    df = read_table_alarmas()
    result = get_mall_cams_alerts(df)
    if not result:
        return no_result
    else:
        return result


