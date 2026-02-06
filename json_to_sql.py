import pyodbc
import json
import os

create_table_query = "CREATE TABLE json_data (id INT IDENTITY(1,1) PRIMARY KEY"

columns=[]

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=test;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

f = open("python/test.json", "r")
data=json.load(f)

for item in data:
    for headinfo in item:
        if headinfo == "properties":
            for i in item[headinfo]:
                if i["property"] not in columns:
                    columns.append(i["property"])
        else:
            if headinfo not in columns:
                columns.append("abmain_" + str(headinfo))

#columns=sorted(columns)
#print(columns)

for col in columns:
    create_table_query += f", [{col}] NVARCHAR(100)"


cursor.execute("DROP TABLE IF EXISTS json_data")
cursor.execute(create_table_query + ")")
cursor.commit()



insert_sql = f"""
INSERT INTO json_data ({", ".join(f"[{c}]" for c in columns)})
VALUES ({", ".join("?" for _ in columns)})
"""

for item in data:
    values = []

    for col in columns:
        val = None

        if col.startswith("abmain_"):
            key = col.replace("abmain_", "")
            if key in item:
                val = item[key]

        else:
            if "properties" in item:
                for p in item["properties"]:
                    if p["property"] == col:
                        val = p["value"]
                        break

        values.append(val)

    cursor.execute(insert_sql, values)

conn.commit()
