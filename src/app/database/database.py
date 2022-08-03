from ast import Pass
import sqlite3, pandas as pd

# class for manipulating database
class db:

    def __init__(self, path=''):
        self.path = path
        conn = sqlite3.connect(self.path)
        conn.close()
    
    def Execute(self, q:str, as_json=False):
        output = []
        try:
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            cur.execute(q)
            if as_json: 
                output = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            else:output = cur.fetchall()
        except Exception as e: print(e)
        finally:
            conn.commit()
            conn.close()
            return output
    
    def ExecuteMany(self, q:str, args:list):
        try:
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            cur.executemany(q, args)
        except Exception as e: print(e)
        finally:
            conn.commit()
            conn.close()
    
    def Execute_pd(self, q:str, as_json = False):
        try:
            conn = sqlite3.connect(self.path)
            df = pd.read_sql_query(q, conn)
        except Exception as e : print(e)
        finally:
            conn.close()
            if as_json: return df.to_json()
            else: return df

    def Init(self, path:str, querie_sep=';'):
        with open(path, 'r') as file:
            qs = file.read().split(sep=querie_sep)
            [self.Execute(q) for q in qs]
    
    def FillTable(self, path:str, table:str, sep=','):
        with open(path, 'r') as file:
            rows = [r.split(sep) for r in [r for r in file.read().split('\n')]] 
            q = "INSERT INTO " + table + " VALUES(" + (len(rows[0])-1)*"?," + " ?);"
            self.ExecuteMany(q, rows)

    def FillTables(self, folder_path:str):
        tables = self.Execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in tables]   
        for table in tables:
            path = folder_path + table + '.csv'
            try:
                self.FillTable(path, table)
            except Exception as e: print(e)

def create_db(paths:dict, init=False):
    # creating our database-object
    a_db = db(paths["database"])
    # initialising our database
    if init :
        a_db.Init(paths["init"]) 
        # filling the rows of our tables of database
        a_db.FillTables(paths["tables"])
    return a_db