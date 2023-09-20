from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import pyodbc 
import time
from .config import settings

server = settings.server_name
database = settings.database_name
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;Encrypt=no'
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})


engine = create_engine(connection_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


###For ODBC Driver
while True:
    try:
        server = 'DESKTOP-O7RP15G\SQLEXPRESS' 
        database = 'studentData' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;Encrypt=no')
        cursor = cnxn.cursor()
        print("connection was successfull")
        break
    except Exception as error:
        print(f"connection failed due to error: {error}")
        time.sleep(2)

