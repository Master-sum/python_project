words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
a = {}
for word in words:
    letter = word[0]
    print(letter)
    if letter not in by_letter:
        by_letter[letter] = [word]
        print([letter])
        print(by_letter)
        a = by_letter.get(letter,word)
        print("------")
        print(a)

print(by_letter)