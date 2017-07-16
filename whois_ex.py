
import whois
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

domain_file = open('domains.txt','r')
ret_file = open('result.json', 'w')

json_data = dict()

line = domain_file.readline().replace("\n","")
while line :
	json_data[line] = whois.query(line).__dict__
	line = domain_file.readline().replace("\n","")

ret_file.write(json.dumps(json_data, default=myconverter))

domain_file.close()
ret_file.close()
