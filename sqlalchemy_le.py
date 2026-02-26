from sql_to_json import result
from matplotlib.pyplot import connect
from ast import stmt
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, insert, select

engine= create_engine("sqlite:///sqlalchemy.db")

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer)

)

metadata.create_all(engine)

# with engine.connect() as conn:
#     s = insert(users).values(name="Jhon",age=5)
#     conn.execute(s)
#     conn.commit()

with engine.connect() as conn:
    s=select(users)
    result = conn.execute(s)

    for row in result:
        print(row[0])
