#打印1-20
for value in range(1,21):
    print(value)
#一百万
numbers = list(range(1,100001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#1到20的奇数
even_numbers = list(range(1,21,2))
for even_number in even_numbers:
    print(even_number)

#3到30能被3整除
even_numbers = list(range(3,31,3))
for even_number in even_numbers:
    print(even_number)

#1到10乘3次方
squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)

#列表解析
squares = [value**3 for value in range(1,11)]
print(squares)