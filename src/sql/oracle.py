#%pip install cx_Oracle --upgrade
import cx_Oracle
import json

#import config

def initoracleclient(instantclient):
    try:
        cx_Oracle.init_oracle_client(lib_dir=instantclient)
    except cx_Oracle.Error as error:
        print(error) 

def queryOracleSql(sql,user,password,url,batch_size=20):
    try: 
        with cx_Oracle.connect(user,password,url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                while True:
                # fetch rows
                    rows = cursor.fetchmany(batch_size)
                    if not rows:
                        break
                # display rows
                    print(json.dumps(rows))
    except cx_Oracle.Error as error:
        print(error) 
