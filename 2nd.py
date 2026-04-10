import pandas as pd

book = [
    {"aouthor":"bhavik", "publish": 2017,"titel":"anyone"},
    {"aouthor":"jash", "publish": 2018,"titel":"jenil's"},
    {"aouthor":"jenil", "publish": 2016,"titel":"virat kohli"},
    {"aouthor":"suhani", "publish": 2020,"titel":"rohit"},
    {"aouthor":"krishna", "publish": 2025,"titel":"riyan parag"},
    {"aouthor":"dharmik", "publish": 2026,"titel":"anfayone"}
]

df = pd.DataFrame(book)
print(df)

df.to_csv("book",index=False)
print("ready to csv")

df_loded = pd.read_csv("book")
print(df_loded)

name = df_loded[df_loded["titel"] == "virat kohli"]
print(f"\n all ane is {name}")