def reversedNum(num):
	str_num = str(num)
	final = ""
	for letter in range(len(str_num) - 1, -1, -1):
		final += str_num[letter]
	return int(final)

print reversedNum(23)
