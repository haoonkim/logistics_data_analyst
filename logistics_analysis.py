import pandas as pd
from sqlalchemy import create_engine

# csv path
csv_path = "/Users/haoonkim/classes/logistics_data_analyst/logistics_data.csv"

df = pd.read_csv(csv_path)

# PostgreSQL connecting
engine = create_engine(
    "postgresql://haoonkim:1234@localhost:5432/postgres"
)



# uploading data
df.to_sql("logistics", engine, if_exists="replace", index=False)

print("데이터 업로드 완료!")

