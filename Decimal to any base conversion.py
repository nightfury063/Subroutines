def decToBaseK(n, k):
	res = ""
	while n>0:
		rem = n%k
		n =n/k
		res += str(rem)
	return int(res[::-1])