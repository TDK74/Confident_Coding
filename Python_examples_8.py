import re
string = 'My name is Rob.'
result = re.search('is (.*).', string)
print(result.group(1))
print('\n')

import re
string = 'The quick brown fox'
result = re.search('The (.*) brown', string)
print(result.group(1))
print('\n')

string = "Rob, Kirsten, Tommy, Ralphie"
print(string.split(","))
print('\n')

string = "<li>John</li> <li>Paul</li> <li>George</li> <li>Ringo</li>"
print(string.split(" "))
print('\n')

string = "<li>John</li> <li>Paul</li> <li>George</li> <li>Ringo</li>"
print(string.split())
print('\n')

import re
string = "<li>John</li> <li>Paul</li> <li>George</li> <li>Ringo</li>"
namesList = string.split()
print(namesList)
for name in namesList:
  print(name)
  result = re.search('<li>(.*)</li>', name)
  print(result.group(1))
print('\n')
