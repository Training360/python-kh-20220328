# def firstn(n):
#     result = []
#     i = 0
#     while i < n:
#         result.append(i)
#         i += 1
#     return result

def firstn(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(sum(firstn(100)))

for n in firstn(20):
    print(n)

print(firstn(100))
result = firstn(100)
print(type(result))