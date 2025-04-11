list1=['mango','banana']
result = list(map(lambda x: "".join(reversed(x)), list1))
print(result)

