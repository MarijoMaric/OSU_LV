'''
1.4.1
def total(radniSati, iznosPoSatu):
    return radniSati*iznosPoSatu

radniSati = float(input("Unesi radne sate: "))
iznosPoSatu = float(input("Unesi iznos po satu: "))
total = total(radniSati, iznosPoSatu)
print(f"Ukupno: {total}")
'''


'''
1.4.2
def getGrade(grade):
    if grade > 0.0 and grade < 0.6:
        return "F"
    if grade >= 0.6 and grade < 0.7:
        return "D"
    if grade >= 0.7 and grade < 0.8:
        return "C"
    if grade >= 0.8 and grade < 0.9:
        return "B"
    if grade >= 0.9 and grade <= 1.0:
        return "A"

try:
    grade = float(input("Unesi ocjenu: "))
    if grade <= 1.0 and grade >= 0.0:
        print(getGrade(grade))
    else:
        print("Unesite unutar intervala")
except ValueError:
    print("Niste unijeli broj!!")
'''

'''
1.4.3
numbers = []
while True:
    try:
        userInput = input("Unesi broj: ")
        if userInput.lower() == "done":
            break
        else:
            num = float(userInput)
            numbers.append(num)
    except ValueError:
        print("Niste unijeli broj!!")

print(f"Uneseno je: {len(numbers)} broja")
avg = sum(numbers) / len(numbers)
print(avg)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
'''
'''
1.4.4
from collections import defaultdict
import re
def count_words(filename):
    word_count = defaultdict(int)

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_count[word] += 1
    return word_count

def unique_words(word_count):
    return {word: count for word, count in word_count.items() if count == 1}

filename = 'song.txt'
word_count = count_words(filename)
unique_word_dict = unique_words(word_count)
print('Riječi koje se pojavljuju: ')
print(word_count)


print(f'Broj riječi koje se pojavljuju samo jednom: {len(unique_word_dict)}')
print('Riječi koje se pojavljuju samo jednom:')
print(unique_word_dict)
'''



ham_words = []
spam_words = []
spam_exclamation_count = 0

with open("SMSSpamCollection.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) < 2:
            continue

        label, message = parts[0], parts[1]
        words = message.split()

        if label == "ham":
            ham_words.extend(words)
        elif label == "spam":
            spam_words.extend(words)
            if message.endswith("!"):
                spam_exclamation_count += 1

average_ham_words = len(ham_words) / sum(1 for line in open("SMSSpamCollection.txt", "r", encoding="utf-8") if line.startswith("ham"))
average_spam_words = len(spam_words) / sum(1 for line in open("SMSSpamCollection.txt", "r", encoding="utf-8") if line.startswith("spam"))

print(f"average_ham_words: {average_ham_words:.2f}")
print(f"average_spam_words: {average_spam_words:.2f}")
print(f"spam_exclamation_count: {spam_exclamation_count}")
