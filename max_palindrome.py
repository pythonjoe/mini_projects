def reversedNum(num):
	str_num = str(num)
	final = ""
	for letter in range(len(str_num) - 1, -1, -1):
		final += str_num[letter]
		print(str_num)
	return int(final)

def maxPal():
	for i in range(999, 0, -1):
		product = i * 999
		if product == reversedNum(product):
			return product

print(maxPal())
