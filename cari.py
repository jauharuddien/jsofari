tkj_2 = [
	'jsofari',
	'akbar'
]

tkj_3 = [
	'mirna',
	'ansi'
]

def search(item,my_list):
	found = False
	position = 0
	while position < len(my_list) and not found:
		if my_list[position] == item:
			found = True
		position = position + 1
	return found 

def tkj2():
	cari = search(item,tkj_2)
	if cari:
		print("XII TKJ 2")


def tkj3():
	cari = search(item,tkj_3)
	if cari:
		print("XII TKJ 3")

item = raw_input("Masukan nama:")
tkj2()
tkj3()
if not tkj2() and not tkj3():
	print("Ooops kami tidak dapat menemukan nama tersebut")
