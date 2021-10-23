import csv
import pandas as pd
from sqlalchemy import create_engine


#put the path to the csv file in a variable
file = 'C:\\Users\\Menna Shazly\\Desktop\\Compiler\\data40000.csv'
chunksize = 500

csv_database = create_engine('sqlite:///C:\\Users\\Menna Shazly\\Desktop\\Compiler\\database.db')
for df in pd.read_csv(file, chunksize=chunksize, iterator=True): 
      df.to_sql('table', csv_database, if_exists='append')