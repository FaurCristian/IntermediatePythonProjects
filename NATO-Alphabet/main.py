import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

ask = True

while ask:
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_phonetic_dic[letter] for letter in word]
        ask = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(output_list)
