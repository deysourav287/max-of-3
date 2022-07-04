m1=int(input('enter the first number'))
m2=int(input('enter the second number'))
m3=int(input('enter the third number'))
if m1>m2 and m1>m3:
	print(m1,'is maximum')
elif m2>m1 and m2>m3:
	print(m2,'is maximum')
elif m3>m1 and m3>m2:
	print(m3,'is maximum')
else:
	print('all numbers are equal')