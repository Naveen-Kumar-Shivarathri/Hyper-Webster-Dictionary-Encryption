inp_fn = raw_input("Enter the file name:")
inp_fs = open(inp_fn,"r")
out_fs = open("scanned_sym.txt","wb+")
out_fs.write("Scanned Symbols\n")
sym_li=[]
count=1
avail = False
sym = inp_fs.read(1)
sym_li.append(ord(sym))
while sym!='':
	if count == 256:
		break
	for x in range(0,count):
		if ord(sym) == sym_li[x]:
			avail = True
			break
		else:
			avail = False
	if avail!=True:
		sym_li.append(ord(sym))
		count = count+1
	sym = inp_fs.read(1)

for x in range(0,count):
	out_fs.write(str(sym_li[x])+'\n')

out_fs.close()
inp_fs.close()
