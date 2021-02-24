list01 = [1,2,3,4,5,6]
list02 = [4,6,7,8,2,7]

A = list01 + list02
A = set(A)
print(A)
print(type(A))

for i in A:
	print(i)
