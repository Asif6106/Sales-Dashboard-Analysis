import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv(r"C:\Users\aasif\OneDrive\Desktop\dataset\Sales_cleaned.csv")
print(df)
engine = create_engine('mysql+pymysql://root:Asif%40123@localhost:3306/salesdb')
df.to_sql(name='sales_data', con=engine, if_exists='replace', index=False)