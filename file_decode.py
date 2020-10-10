import decoder

inp_fn = raw_input("Enter the file name to decode:")
inp_fs = open(inp_fn,"r")
out_fs = open("decoded_file.txt","wb+")

enc_ln = int(inp_fs.readline())
st_to_dec = inp_fs.readline()

while st_to_dec!='':
	out_fs.write(decoder.decode(enc_ln,int(st_to_dec)))
	st_to_dec = inp_fs.readline()

out_fs.close()
inp_fs.close()
