from functools import cmp_to_key
mp = {}
def comp(a, b):
	for i in range( min(len(a), len(b))):
		
	
		if (mp[a[i]] != mp[b[i]]):
			if mp[a[i]] < mp[b[i]]:
				return -1
			else:
				return 1
	
	if (len(a) < len(b)):
		return -1
	else:
		return 1


def printSorted(words, order):
	
	
	for i in range(len(order)):
		mp[order[i]] = i
	
	words = sorted(words, key = cmp_to_key(comp))
	
	
	for x in words:
		print(x, end = " ")

words = [ "word", "world", "row" ]
order = "worldabcefghijkmnpqstuvxyz"

printSorted(words, order)


