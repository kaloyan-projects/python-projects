chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

num = input("Enter value: ")
inbase = int(input("Enter base of input: "))
outbase = int(input("Enter base of output: "))

if not 2 <= inbase <= len(chars) or not 2 <= outbase <= len(chars):
	raise Exception("Base doesn't exist!")

def other_to_base_ten(num, base):
	result = 0
	positive = True
	if num[0] == '-':
		positive = False
		num = num[1:]

	for i, n in enumerate(num[::-1]):
		if chars.index(n) > base-1:
			raise Exception("Sign does not exist in this base!")
		n = n.upper()
		result += chars.index(n) * base ** i

	if not positive:
		result = -1 * result

	return result

def base_ten_to_other(n, b):
	negative = False
	if n == 0:
		return [0]
	elif n < 0:
		n *= -1
		negative = True
	digits = []
	while n:
		digits.append(chars[int(n % b)])
		n //= b
	if not negative:
		return "".join(map(str, digits[::-1]))
	else:
		return "-"+"".join(map(str, digits[::-1]))

print("Output:",base_ten_to_other(other_to_base_ten(num, inbase), outbase))
