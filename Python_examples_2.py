names = ["Name1", "Name2", "Name3", "Name4"]
print(names)
print(names[0])
print(names[2])
print('\n')

flavours = ["strawberry", "chocolate", "vanilla", "mint choc chip"]
print(flavours[3])
print(flavours[0])
print(flavours[1] + " and " + flavours[2])
print('\n')

flavours[2] = "rum and raisin"
print(flavours)
flavours.remove("strawberry")
print(flavours)
flavours.pop(0)
print(flavours)
flavours.insert(1, "lemon sorbet")
print(flavours)
print('\n')
