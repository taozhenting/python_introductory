#按字母排列（永久）
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#按字母反顺序排列（永久）
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#按字母排列（临时）
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#相反顺序排列（永久），想恢复再次reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))