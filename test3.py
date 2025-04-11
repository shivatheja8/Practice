list1=['apple','orange']
result = list(map(lambda x: "".join(reversed(x)), list1))
print(result)

