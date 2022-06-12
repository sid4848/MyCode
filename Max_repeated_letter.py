# Here we ae going to find mac repeated letter in any sentence
sentence = "This is common interview question"
letters = [*sentence]

data = [(i,letters.count(i)) for i in letters]

def find_max(letter):
    return letter[1]

data.sort(key = find_max)
max_repeated = data[len(data) - 1]
print("Max repeated letter: ", max_repeated[0])
print("Count: ",max_repeated[1])
