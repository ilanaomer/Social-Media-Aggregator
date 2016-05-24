from collections import Counter

def check_words(filename, tests):
    results = Counter()
    with open(filename) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            for k, v in tests.items():
                results[k] += 1 if v(s) else 0
            results.most_common()
    return results

tests = {
    "Words with more than 3 letters": lambda w: len(w) > 3,
    "Word starts with a vowel": lambda w: (w[0] in ('a', 'e', 'i', 'o', 'u')),
    "Word ends with a vowel": lambda w: w[-1] in ('a', 'e', 'i', 'o', 'u'),
    "All words. (Test always passes)": lambda w: True,
    "Word has only vowels": lambda w: all(c in ('a', 'e', 'i', 'o', 'u') for c in w),
    "Word does not have any vowel": lambda w: not any(c in ('a', 'e', 'i', 'o', 'u') for c in w),
    "Word is a palindrome": lambda w: w == w[::-1],
    "Word has two identical letters consecutively": lambda w: any(w[i] == w[i+1] for i in range(len(w)-1)),
    "Word has three identical letters consecutively": lambda w: any(w[i] == w[i+1] == w[i+2] for i in range(len(w)-2)),
}

results = check_words('wordsEn.txt', tests)
for k, v in results.items():
    print(k, v)
