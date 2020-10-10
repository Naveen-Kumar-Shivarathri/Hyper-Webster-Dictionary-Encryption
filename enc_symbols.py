sym_fs = open("scanned_sym.txt","r")
temp = sym_fs.readline()	
switcher= {}
count=1
inp_sym = sym_fs.readline()
while inp_sym!='':
	inp_sym = int(inp_sym)
	inp_sym = inp_sym+1
	switcher[inp_sym]=count
	count=count+1
	inp_sym = sym_fs.readline()
sym_fs.close()
def sym_trans(i):
	return switcher.get(i)
enc_sym_nu = count


