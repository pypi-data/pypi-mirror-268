import pandas as pd
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData,Date,DateTime,Time
import mysql.connector
import numpy as np

def listBase():
    address='mysql+mysqlconnector://root:tiger1006@localhost/'
    engine = create_engine(address)
    # execute query to get all databases
    result_set = engine.execute("SHOW DATABASES")

    # print the list of databases
    for row in result_set:
        print(row[0])

def listTable(sql):
    address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
    engine = create_engine(address)
    # get the metadata of the macrodata
    metadata = MetaData(bind=engine)

# reflect the macrodata and retrieve the table names
    metadata.reflect()
    table_names = metadata.tables.keys()

    # print the table names
    for table_name in table_names:
        print(table_name)

def createBase(sql):
    address='mysql+mysqlconnector://root:tiger1006@localhost/'
    engine = create_engine(address)
    engine.execute("CREATE DATABASE "+sql)
def createTable(sql,table,col_list,type_list):
    address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
    engine = create_engine(address)
    # Create a metadata object that will hold the definition of the table
    metadata = MetaData()
    my_table=Table(table,metadata,Column(col_list[0],type_list[0]))
    
    if len(col_list)>1:
        for i in range(1,len(col_list)):
            new_col=Column(col_list[i],type_list[i])
            my_table.append_column(new_col)
    
    metadata.create_all(engine)
    
  

def deleteBase(sql):
    address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
    engine = create_engine(address)
    metadata = MetaData()

# associate the metadata with the engine
    metadata.bind = engine

# drop all tables associated with the metadata
    metadata.drop_all(bind=engine)
    
    
def deleteTable(sql,table):
    address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
    engine = create_engine(address)

    connection = engine.connect()

    table_name = table
    query = f"DROP TABLE IF EXISTS {table_name};"
    connection.execute(query)

    connection.close()
    
    


def df2table(sql,df,table,flag,chunk=10000):
    '''
    chunk is the size for batch save. by default 10000
    -------
    flag:  
    -------
    we're using 'replace' to replace the existing table with the new data.
    You can also use 'append' to add the new data to the existing table 
    or 'fail' to raise an error if the table already exists.
    '''
    address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
    engine = create_engine(address)
    df.fillna(value='NULL',inplace=True)
    
    df.to_sql(table, con=engine, chunksize=chunk,if_exists=flag, index=False)

def table2df(sql,table,condition=None):
    '''
    condition: "country = 'us'"
    table:  "investing"
    sql: ""macro""
    '''
    if condition==None:
        address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
        engine = create_engine(address)
        query = "SELECT * FROM "+ table
        df = pd.read_sql(query, engine)

        return df.replace(to_replace='NULL',value=np.nan)

    else:
        address='mysql+mysqlconnector://root:tiger1006@localhost:3306/'+sql
        engine = create_engine(address)
        query = "SELECT * FROM "+ table+" WHERE "+condition
        df = pd.read_sql(query, engine)

        return df.replace(to_replace='NULL',value=np.nan)


def downloadfromsql(database,table,indexcol):
    data = table2df(database, table).set_index(indexcol)
    data.index=pd.to_datetime(data.index)
    return data.sort_index()
 