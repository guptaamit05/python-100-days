import pandas as pd


df = pd.read_csv("./nato_phonetic_alphabet.csv")
rows = {value.letter:value.code for (new_key,value) in df.iterrows()}
# print(rows)

user_input = input("enter any name: \n").upper()
result = {x:rows[x] for x in user_input if x in rows.keys()}

print(result)

