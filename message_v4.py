import pyodbc
import pandas as pd
import datetime
import json
import time

start = time.time()
now = datetime.datetime.utcnow()

# lista todas las cam_id asignadas a los malls
#json no acepta int64 asique se tarbaja en str
m1=set([str(x) for x in range (76,85)])
m2=set([str(x) for x in range (85,94)])
m3=set([str(x) for x in range (30,40)])
m4=set([str(x) for x in range (40,50)])
m5=set([str(x) for x in range (50,60)])
m6=set([str(x) for x in range (60,70)])

malls_dic = {'Mall 1':m1,'Mall 2':m2,'Mall 3':m3,'Mall 4':m4,'Mall 5':m5,'Mall 6':m6}

no_result = {'Mall 1':[], 'Mall 2':[], 'Mall 3':[], 'Mall 4':[], 'Mall 5':[], 'Mall 6':[]}

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

query = pd.read_sql_query(
            'select * from alerta_alarmas where id_alarma in (select max(id_alarma) as id_alarm from alerta_alarmas group by camara_id)', cnxn)

query['camara_id'] = query['camara_id'].astype(str) #json no acepta el int64 asique se genera en str
#times = pd.to_datetime(query['fecha_alarma']).sort_values()
#print(times.values[-1])

#now = pd.to_datetime(times.values[-1])
#now = pd.to_datetime(query['fecha_alarma'][0])
#print(now)

def checkTime(df,ss=30,mm=0,hh=0):
    delta = datetime.timedelta(seconds=ss,minutes=mm,hours=hh)
    start_t = now - delta
    end_t = now + delta
    #print(df)
    #print(start_t,now,end_t)

    mask = (df['fecha_alarma'] >= start_t) & (df['fecha_alarma'] <= end_t)

    new_df = df.loc[mask]
    return new_df

#obtenemos id mall y camaras con alarma del modo {1:'0',...'5'} donde solo estan los que existen
def get_mall_cams_alerts(df, malls = malls_dic):
    result = dict()
    #new_alerts = checkTime(df)
    print(df)
    # obtenemos solo los cam id distintos en el objeto diff_ids
    diff_ids = set(df.camara_id.unique())
    for id_mall, cam_ids in malls.items():
        common_cam_ids = cam_ids.intersection(diff_ids)
        ids = list(common_cam_ids)
        result[id_mall] = ids
    print(f'Result: {result}')
    return result

def main(df = query):
    result = get_mall_cams_alerts(df)
    if not result:
        json_file = json.dumps(no_result, indent = 4)
        with open('alarmas.json', 'w', encoding = 'utf-8') as f:
            json.dump(no_result, f, ensure_ascii = False, indent = 4)
    else:
        json_file = json.dumps(result, indent = 4)
        with open('alarmas.json', 'w', encoding = 'utf-8') as f:
            json.dump(result, f, ensure_ascii = False, indent = 4)

main()
end=time.time()
print('tiempo de ejecucion: ', end-start,' s')


