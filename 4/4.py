def find_password(lower, upper):
	return [x for x in range(lower, upper + 1) 
				if has_two_adjacent_digits(x)
				and has_monotonic_digits(x)]

def has_two_adjacent_digits(n):
	for i in [str(k) for k in range(10)]:
		if len(str(n).replace(i, '')) == 4:
			return True
	return False
	# return any([len(str(n).replace(i, '')) == 4 for i in [str(k) for k in range(10)]])

def has_monotonic_digits(n):
	digits = [int(k) for k in str(n)]
	return digits == sorted(digits)

print(len(find_password(138241, 674034)))

# or i guess you could do a one-liner:
# print(len([x for x in range(138241, 674035) if any([len(str(x).replace(i, '')) == 4 for i in [str(k) for k in range(10)]]) and [int(k) for k in str(x)] == sorted([int(k) for k in str(x)])]))