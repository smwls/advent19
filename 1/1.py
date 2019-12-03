#!/usr/bin/python3

from math import floor

def fuel(m):
	tot = 0
	current = floor(int(m) / 3) - 2
	while current > 0:
		tot += current
		current = floor(int(current) / 3) - 2
	return tot

with open('1', 'r') as f:
	masses = f.read().split()	
	total_fuel = [fuel(m) for m in masses]
	print(sum(total_fuel))

