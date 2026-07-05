word = input("Enter a word: ")
count = {}

for ch in word:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for ch in word:
    if count[ch] == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character found")