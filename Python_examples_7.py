numbers = [8, 3, 5, 7, 0, 13, 20]
for number in numbers:
  if number > 7:
    print (number)
print('\n')

numbers = [7, 3, 4, 3, 8, 2, 1, 1, 2, 7, 8]
print(numbers)
alreadyPrintedNumbers = []
for number in numbers:
  alreadyPrinted = False
  for alreadyPrintedNumber in alreadyPrintedNumbers:
    if number == alreadyPrintedNumber:
      alreadyPrinted = True
  if alreadyPrinted == False:
    print(number)
    alreadyPrintedNumbers.append(number)
print(alreadyPrintedNumbers)
print('\n')
