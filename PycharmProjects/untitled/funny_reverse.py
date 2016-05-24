def funny(s):
    return " ".join([(x[::-1]).title() for x in s.split()])



result = funny("Foo bar")
print(result)
assert result == "Oof Rab"

result = funny("The quick brown fox")
print(result)
assert result == "Eht Kciuq Nworb Xof"

print("OK")