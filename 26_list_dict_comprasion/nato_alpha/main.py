import pandas as pd


df = pd.read_csv("./nato_phonetic_alphabet.csv")
rows = {value.letter:value.code for (new_key,value) in df.iterrows()}
# print(rows)

def generate_phonetic():
    user_input = input("enter any name: \n").upper()
    try:
        # result = [rows[x] for x in user_input if x in rows.keys()]
        result = [rows[x] for x in user_input]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()        
    else:
        print(result)

generate_phonetic()