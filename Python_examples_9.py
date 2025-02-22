import urllib.request
import re

names = []
addresses = []
emailAddresses = []
phoneNumbers = []

page = urllib.request.urlopen('http://wwww.robpercival.co.uk/sampledata.html')
# print(page.read())
# print('\n')

page = urllib.request.urlopen('http://wwww.robpercival.co.uk/sampledata.html')
string = page.read().decode('utf-8')

rowList = string.split("<tr>")
# print(rowList)
# print('\n')

for row in rowList:
  rowContentList = row.split("\n")
  # print(rowContentList)

  i = 0

  for lineOfHTML in rowContentList:
    if "<td>" in lineOfHTML:
      s = re.search("<td>(.*)</td>", lineOfHTML)
      # print(s.group(1))

      if i == 0:
        names.append(s.group(1))
      elif i == 1:
        addresses.append(s.group(1))
      elif i == 2:
        emailAddresses.append(s.group(1))
      else:
        phoneNumbers.append(s.group(1))
      i = i + 1

print(names)
print(addresses)
print(emailAddresses)
print(phoneNumbers)
