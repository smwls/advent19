def find_password(lower, upper):
	return [x for x in range(lower, upper + 1) 
				if has_two_adjacent_digits(x)
				and has_monotonic_digits(x)]

def has_two_adjacent_digits(n):
	strn = str(n)
	for i in [str(k) for k in range(10)]:
		if len(strn.replace(i, '')) == 4:
			return True
	return False

def has_monotonic_digits(n):
	digits = [int(k) for k in str(n)]
	return digits == sorted(digits)

print(len(find_password(138241, 674034)))