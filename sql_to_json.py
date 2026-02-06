import pyodbc
import json
import os

result = []

column_names = []

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=test;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM json_data")
rows = cursor.fetchall()

for col in cursor.description:
    column_names.append(col[0])

for row in rows:

    item = {}
    properties = []

    col_index = 0
    for col_name in column_names:

        value = row[col_index]
        col_index += 1

        if value is None:
            continue

        if col_name == "id":
            continue

        if col_name.startswith("abmain_"):

            json_key = col_name.replace("abmain_", "")
            item[json_key] = str(value)

        else:

            prop = {}
            prop["property"] = col_name
            prop["value"] = str(value)
            properties.append(prop)

    item["properties"] = properties
    result.append(item)

print(json.dumps(result, indent=4))