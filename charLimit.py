listoffinal = []

f = open("input", "r+")

repeatTime = 0

numberoflines = len(f.readlines())

print(len(f.readlines()))
f.seek(0)
while repeatTime < numberoflines:
	listofcharacters = []
	
	message = f.readline()
#a placeholder to determine how far you are in a loop
	value = 0
#same use as "value"
	placeValue = 0
#list of characters
	while value < len(message):
		character = message[placeValue]
		listofcharacters.append(character)
		value = value + 1
		placeValue = placeValue + 1
	print(listofcharacters)
	value = len(listofcharacters)
#tests for over ten
	if len(listofcharacters) > 10:
		while value > 10:
			listofcharacters.pop(value-1)
			value = len(listofcharacters)
		listofcharacters.append("\n")
	value = 0
#appends into a final list
	while value < len(listofcharacters):
		listoffinal.append(listofcharacters[value])
		value = value + 1
	repeatTime = repeatTime + 1
