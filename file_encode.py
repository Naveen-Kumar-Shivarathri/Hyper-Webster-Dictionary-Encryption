import encoder

inp_fn = raw_input("Enter the file name to encode:")
enc_ln = input("Enter the encoding length:")
sp_fn = inp_fn.split('.')
input_fs = open(inp_fn,"r")
rank_fs = open("encoded_"+sp_fn[0]+'_'+sp_fn[1]+".vpe","wb+")
rank_fs.write(str(enc_ln)+"\n")

data_chunk = input_fs.read(enc_ln)


while data_chunk!='':
	if len(data_chunk)!=enc_ln:
		for x in range(0,enc_ln-len(data_chunk)):
			data_chunk=data_chunk+'\0'
		enc_rank = encoder.encode(data_chunk)
		rank_fs.write(str(enc_rank)+"\n")
		data_chunk = input_fs.read(enc_ln)
	else:
		enc_rank = encoder.encode(data_chunk)
		rank_fs.write(str(enc_rank)+"\n")
		data_chunk = input_fs.read(enc_ln)


input_fs.close()
rank_fs.close()



#plt.scatter(sorted(so_key),so_rnk,s=3,color="#0000ff",label="rank curve")
#plt.scatter(sorted(so_key),so_key,s=5,color="#ff0000",label="key curve")
#plt.legend()
#plt.show()
