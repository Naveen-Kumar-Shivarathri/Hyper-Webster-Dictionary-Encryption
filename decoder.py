import dec_symbols
def decode(enc_lt,enc_rn):	
	no_of_sym = dec_symbols.dec_sym_nu
	decoded_ls = []
	s1 = (no_of_sym*(no_of_sym**(enc_lt-1)-1))/(no_of_sym-1)
	net_sum = enc_rn - s1
	la_char = net_sum%no_of_sym
	net_sum = net_sum-la_char
	enc_lt = enc_lt-1
	for cycle in range(0,enc_lt):
		temp = net_sum/(no_of_sym**(enc_lt-cycle))
		temp_char = dec_symbols.sym_trans(temp+1)
		decoded_ls.append(temp_char)
		net_sum = net_sum-temp*(no_of_sym**(enc_lt-cycle))
	
	temp_char = dec_symbols.sym_trans(la_char)
	decoded_ls.append(temp_char)
	
	decoded_str = "".join([str(elem) for elem in decoded_ls])
	return decoded_str
