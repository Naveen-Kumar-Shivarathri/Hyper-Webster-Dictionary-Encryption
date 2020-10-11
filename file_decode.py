import decoder

inp_fn = raw_input("Enter the file name to decode:")
sp_fn_a = inp_fn.split('.')
sp_fn_b = sp_fn_a[0].split('_')
inp_fs = open(inp_fn,"r")
out_fs = open("decoded_"+sp_fn_b[1]+'.'+sp_fn_b[2],"wb+")

enc_ln = int(inp_fs.readline())
st_to_dec = inp_fs.readline()

while st_to_dec!='':
	out_fs.write(decoder.decode(enc_ln,int(st_to_dec)))
	st_to_dec = inp_fs.readline()

out_fs.close()
inp_fs.close()
