import json
with open("node_modules/profane-words/words.json", "r") as f:
    banned_words = json.load(f)
    banned_words = {word.lower() for word in banned_words}

five_letter_words = []
for word in banned_words:
    if len(word) == 5 and word.isalpha():
        five_letter_words.append(word)
print(five_letter_words)

clean_words = []
with open("google+dev/valid-wordle-words.txt", "r") as f:
    for line in f:
        word = line.strip().lower()
        if word and word not in banned_words:
            clean_words.append(word)

with open("google+dev/clean-words.txt", "w") as f:
    for word in clean_words:
        f.write(word + "\n")

print(clean_words)