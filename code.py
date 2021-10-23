import csv
import pandas as pd
from sqlalchemy import create_engine


#A class that can read a zipped csv/txt file or from a given connection string to a sqlite DB, 
#filters, and selects named/numbered columns.
class cls_DS_class:

      @staticmethod
      def csv_sql():
            file_path = "C:\\Users\\Menna Shazly\\Desktop\\Compiler\\data40000.zip"
            chunksize = 1000

            #create sqlLite database
            csv_database = create_engine('sqlite:///C:\\Users\\Menna Shazly\\Desktop\\Compiler\\csv_database.db')

            #read the csv file and put it into the database
            for df in pd.read_csv(file_path, chunksize=chunksize, iterator=True): 
                  df.to_sql('table', csv_database, if_exists='append', index=False)



#test Cases
cls_DS_class.csv_sql()