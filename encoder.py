import enc_symbols
	
def encode(inp):
	sum=0
	s1 = 0
	s2 = 0
	count=1
	ch_len = len(inp)
	no_of_sym=enc_symbols.enc_sym_nu
	s1 = (no_of_sym*(no_of_sym**(ch_len-1)-1))/(no_of_sym-1)
	
	for inp_sym in inp:
		sym_to_enc = ord(inp_sym)
		sym_to_enc = sym_to_enc+1
		if count == ch_len:
			s2=s2+(enc_symbols.sym_trans(sym_to_enc))*(no_of_sym**(ch_len-count))
		else:
			s2=s2+(enc_symbols.sym_trans(sym_to_enc)-1)*(no_of_sym**(ch_len-count))
		count = count+1;
	
	sum = s1+s2;
	return sum
	
	
