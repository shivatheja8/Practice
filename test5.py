str1 = 'abcdef'
str2 = 'defghia'

matching = 0

for i in str1:
  for j in str2:
    if i == j:
      matching += 1

print("total same letter =", matching)