from itertools import combinations

def all_variants(text):
    i = 0
    while i <= len(text):
        for l in combinations(text, i + 1):
            yield ''.join(l)
        i += 1

a = all_variants("abc")
for i in a:
    print(i)

