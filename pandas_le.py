# ==========================================
# EXTREME PANDAS EXAMPLES FILE
# ==========================================

import pandas as pd
import numpy as np

# ==========================================
# DATA SETUP
# ==========================================

df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 29],
    "salary": [500, 600, 700, 800, 550],
    "dept": ["IT", "HR", "IT", "Finance", "HR"],
    "date": pd.date_range("2024-01-01", periods=5)
})

# print(df)

# # ==========================================
# # SERIES OPERATIONS
# # ==========================================

# s = pd.Series([10, 20, 30, 40])

# print(s + 5)
# print(s * 2)
# print(s[s > 20])
# print(s.iloc[1:3])
# print(s.values)
# print(s.index)

# # ==========================================
# # SELECTION DEEP DIVE
# # ==========================================

# print(df.loc[0])                        # row
# print(df.loc[0:3,['id','name','age']])               # single value
# print(df.loc[:, ["name", "salary"]])   # columns
# print(df.iloc[0:3, 1:4])               # slicing

# # Boolean selection
# print(df[df["salary"] > 550])

# # Multiple conditions
# print(df[(df["age"] > 25) & (df["dept"] == "IT")])
# print(df[(df['age'] > 25) & (df['dept'] == 'IT')])


# # isin
# print(df[df["dept"].isin(["IT", "HR"])])

# # ==========================================
# # COLUMN OPERATIONS
# # ==========================================

# df["bonus"] = df["salary"] * 0.2
# df["salary_log"] = np.log(df["salary"])

# df["category"] = np.where(df["salary"] > 600, "High", "Low")

# df["combined"] = df["name"] + "_" + df["dept"]

# print(df)
# # ==========================================
# # APPLY / MAP / TRANSFORM
# # ==========================================

# print(df["salary"].apply(lambda x: x * 2))

# print(df["dept"].map({"IT": "Tech", "HR": "Human", "Finance": "Fin"}))

# df['avgs'] = df.groupby("dept")["salary"].transform("mean")

# print(df)
# # ==========================================
# # SORTING ADVANCED
# # ==========================================

# print(df.sort_values(by=["dept", "salary"], ascending=[True, False]))

# # ==========================================
# # GROUPBY ADVANCED
# # ==========================================

g = df.groupby("dept")

# print(g["salary"].sum())
# print(g["salary"].mean())

# Multiple aggregations
# print(g.agg({
#     "salary": ["sum", "mean", "max"],
#     "age": ["min", "max"]
# }))

# # Custom aggregation
# print(g["salary"].agg(lambda x: x.max() - x.min()))

# # ==========================================
# # FILTER WITH GROUPBY
# # ==========================================

# print(g.filter(lambda x: x["salary"].mean() > 600))

# # ==========================================
# # PIVOT / PIVOT_TABLE
# # ==========================================

# pivot = df.pivot_table(
#     values="salary",
#     index="dept",
#     aggfunc=["mean", "sum"]
# )
# print(pivot)

# # ==========================================
# # MERGE / JOIN VARIANTS
# # ==========================================

df2 = pd.DataFrame({
    "dept": ["IT", "HR", "Finance"],
    "manager": ["John", "Sara", "Mike"]
})

# Inner
# print(pd.merge(df, df2, on="dept", how="inner"))

# # Left
# print(pd.merge(df, df2, on="dept", how="left"))

# # Right
# print(pd.merge(df, df2, on="dept", how="right"))

# # Outer
# print(pd.merge(df, df2, on="dept", how="outer"))

# # ==========================================
# # CONCAT VARIANTS
# # ==========================================

# df_concat_rows = pd.concat([df, df])
# df_concat_cols = pd.concat([df, df2], axis=1)

# print(df_concat_rows.reset_index(drop=True))
# print(df_concat_cols)
# # ==========================================
# # MISSING DATA
# # ==========================================

# df.loc[0, "salary"] = np.nan

# print(df.isnull().sum())
# print(df.fillna(0))
# # print(df.fillna(method="ffill"))
# print(df.dropna())

# # ==========================================
# # DUPLICATES
# # ==========================================

# df_dup = pd.concat([df, df]).reset_index(drop=True)
# print(df_dup.duplicated())
# print(df_dup.drop_duplicates())

# # ==========================================
# # STRING METHODS
# # ==========================================

# df["name"].str.lower()
# df["name"].str.upper()
# df["name"].str.len()
# df["name"].str.contains("a", case=False)
# df["name"].str.replace("a", "X", regex=True)
# df["name"].str.split("e")

# # ==========================================
# # DATETIME METHODS
# # ==========================================

# df["year"] = df["date"].dt.year
# df["month"] = df["date"].dt.month
# df["day"] = df["date"].dt.day

# print(df.set_index("date").resample("M").mean(numeric_only=True))

# # ==========================================
# # WINDOW FUNCTIONS
# # ==========================================

# print(df["salary"].rolling(2).mean())
# print(df["salary"].expanding().sum())

# # ==========================================
# # RANK / SHIFT / DIFF
# # ==========================================

# df["rank"] = df["salary"].rank()
# df["shift"] = df["salary"].shift(1)
# df["diff"] = df["salary"].diff()

# print(df)
# # ==========================================
# # BOOLEAN MASKING ADVANCED
# # ==========================================

# mask = (df["salary"] > 500) & (df["age"] < 40)
# print(df.loc[mask, ["name", "salary"]])

# # ==========================================
# # VALUE COUNTS / UNIQUE
# # ==========================================

# print(df["dept"].value_counts())
# print(df["dept"].unique())
# print(df["dept"].nunique())

# # ==========================================
# # CLIP / CUT / QCUT
# # ==========================================

# df["salary_clip"] = df["salary"].clip(upper=700)

# df["bins"] = pd.cut(df["salary"], bins=3)

# df["quantiles"] = pd.qcut(df["salary"], q=3)
# print(df)

# # ==========================================
# # RESHAPING (MELT / STACK / UNSTACK)
# # ==========================================

# melted = df.melt(id_vars=["id"], value_vars=["salary", "age"])
# print(melted)
# stacked = df.set_index(["id", "dept"]).stack()
# print(stacked)
# unstacked = stacked.unstack()
# print(unstacked)

# # ==========================================
# # INDEX OPERATIONS
# # ==========================================

# df2 = df.set_index("id")
# df2.reset_index()

# df.rename(columns={"salary": "salary_new"}, inplace=True)

# # ==========================================
# # QUERY
# # ==========================================

# print(df.query("salary > 500 and age < 40"))

# # ==========================================
# # SAMPLE / RANDOM
# # ==========================================

# print(df.sample(n=2))
# print(df.sample(frac=0.5))

# # ==========================================
# # NUMPY INTEROP
# # ==========================================

# print(np.mean(df["salary"]))
# print(np.sqrt(df["salary"]))

# # ==========================================
# # PERFORMANCE TIPS (IMPORTANT)
# # ==========================================

# # vectorized (FAST)
# df["fast"] = df["salary"] * 2

# # avoid loops (SLOW)
# # for i in range(len(df)):
# #     df.loc[i, "slow"] = df.loc[i, "salary"] * 2

# # ==========================================
# # END
# # ==========================================      