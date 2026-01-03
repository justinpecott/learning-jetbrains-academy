from itertools import permutations

chunks = ["se", "par", "st", "ati"]
words = ["".join(p) for p in permutations(chunks)]

for word in sorted(set(words)):
    print(word)
