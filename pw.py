password = 'a123456'
r = 0
while r < 3:
	pw1 = input('pls type pw: ')
	if pw1 == password:
		print('pass')
		break
	elif pw1 != password:
		r = r + 1
		print('try again only have', 3 - r,'time')