def word_lengths(s):
    return [len(x) for x in s.split()]



result = word_lengths("Contrary to popular belief Lorem Ipsum is not simply random text")
print("Result:", result)
assert result == [8, 2, 7, 6, 5, 5, 2, 3, 6, 6, 4]
print("OK")

def max_word_length(s):
    return max(word_lengths(s))

result = max_word_length("Contrary to popular belief Lorem Ipsum is not simply random text")
print("Result:", result)
assert result == 8
print("OK")