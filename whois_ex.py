import  whois

domain_file = open('domains.txt','r')
ret_file = open('result.txt', 'w')


l = domain_file.readline()
while l:

	ret_file.write("{")
	domain_info = whois.query(l).__dict__
	
	key_list = list(domain_info)
	value_list = list(domain_info.values())
	json_val = []
	for i in range(len(value_list)):
		json_val.append(repr(key_list[i])+":"+repr(value_list[i]))
	for item in json_val:
		if item != json_val[-1]: 
			ret_file.write(item)
			ret_file.write(", ")
		else:
			ret_file.write(item)

	ret_file.write("}\n")

	l = domain_file.readline()


domain_file.close()
ret_file.close()
