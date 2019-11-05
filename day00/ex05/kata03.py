phrase = "The right format"

s = ""
for i in range(42 - len(phrase)):
    s = s + "-"
print(s + phrase, end="")
