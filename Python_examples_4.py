for x in range (0, 3):
  print (x)
print('\n')

for x in range (0, 11):
  print(3 * x)
print('\n')

for x in range (0, 21):
  print(5 * x)
print('\n')

for x in range (0, 5):
  print(5 - x)
print('\n')

ages = [36, 35, 5, 1]
for age in ages:
  print(age)
print('\n')

print(len(ages))
print('\n')

for i in range (0, len(ages)):
  ages[i] = ages[i] + 1
print(ages)
print('\n')

numbers = [10, 20, 30, 40, 50]
for i in range (0, len(numbers)):
  numbers[i] = numbers[i] * 2
print(numbers)
print('\n')

beatles = ["John", "Paul", "Ringo", "George"]
for name in beatles:
  print("Hello " + name)
print('\n')
