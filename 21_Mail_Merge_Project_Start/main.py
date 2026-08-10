PLACEHOLDER_TEXT = '[name]'

with open("./input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()

letter_content=""
with open("./input/Letters/starting_letter.txt", 'r') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER_TEXT, name)
        with open(f"./Output/ReadyToSend/letter_of_{name}.txt", 'w') as each_name:
            each_name.write(new_letter)
        
