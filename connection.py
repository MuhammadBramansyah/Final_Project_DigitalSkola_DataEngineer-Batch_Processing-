import json
from time import time
import psycopg2

def param_config(config):
    with open("config.json","rb") as file:
        conf = json.load(file)

    try:
        conf = conf[config]
        return conf
    except:
        print("check config")

def postgres_conn(conf):
    while True:
        try:
            conn = psycopg2.connect(
                host = conf["host"],
                user = conf["user"],
                password = conf["password"],
                database = conf["database"],
                port = conf["port"])
            break
        except:
            print("cek config this ...")
            time.sleep(1)
    return conn
