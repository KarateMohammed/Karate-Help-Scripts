import datetime

if __name__ == '__main__':
	print ("Main_1")


if not __name__ =='__main__' :
	print ("Main_1 not run directly")



num={}
num={"a":{"odd":1,"even": 2},"b" :{"odd":3 ,"even": 4},"c":{"odd":5,"even": 6},"d":{"odd":7,"even": 8},"s":{"odd":9,"even": 10}}

print (num)

print("num.values")
print(num.values())
print(type(num.values()))
print("")

dict_value=num.values()
print("dict_value")
print(dict_value)
print("")


print("num.items")
print(num.items())
print("")

print("num.keys()")
print(num.keys())
Dict_Keys=num.keys()
for i in  Dict_Keys :
	print (i)

print("num.items")
for x,y in num.items():
	print(f"Key {x} Value {y}")


Temp_Dict_Username={"odd":11}
Temp_Dict_Pass ={"even":''}
Temp_Dict_Enable =""
Ip="f"

Temp_Dict_IP={}
Temp_Dict_IP[Ip]={}
Temp_Dict_IP[Ip].update(Temp_Dict_Username)
Temp_Dict_IP[Ip].update(Temp_Dict_Pass)

print("")
print("Temp_Dict_IP")
print(Temp_Dict_IP)
num.update(Temp_Dict_IP)
print("")
print("num")
print(num)

print('')
print(num['a']['odd'])

num.update({"l":{"odd":1003,"even": 1000}})

import os
import os.path
import json

def Append_to_Old_File(fullpath='' ,Unknown_Lists=[]) :
	with open(fullpath, 'a') as file:
		for i in Unknown_Lists:
			file.write((str(i)+"\n"))
	os.chmod(fullpath, 0o777)  ## to use it with full permisson
	file.close()


Dict_all_IP_Usr_Pass_Ena={}
ip="123"
Temp_Dict_k_ip={}
Temp_Dict_k_ip[ip]={}
Device_Type=[]
Username_Device=[]
Passowrd_Device=[]
Device_Type_Num=0
User_Pass_Num=0
Device_Type=['mohammed']
Passowrd_Device=['Mohammed']
Username_Device=['Password']
Temp_Dict_Connection_type={"Connection_type":Device_Type[Device_Type_Num]}
Temp_Dict_k_Username={"k_Username":Username_Device[User_Pass_Num]}
Temp_Dict_k_Password={"k_Password":Passowrd_Device[User_Pass_Num]}
Temp_Dict_k_Enable={"k_Enable":''}

Temp_Dict_k_ip[ip].update(Temp_Dict_Connection_type)
Temp_Dict_k_ip[ip].update(Temp_Dict_k_Username)
Temp_Dict_k_ip[ip].update( Temp_Dict_k_Password)
Temp_Dict_k_ip[ip].update(Temp_Dict_k_Enable)
Dict_all_IP_Usr_Pass_Ena.update(Temp_Dict_k_ip)
print (f"Dict_all_IP_Usr_Pass_Ena[{ip}]")
print (Dict_all_IP_Usr_Pass_Ena[ip])
# Temp_Dict_k_ip.popitem()
Temp_Dict_k_ip={}
print("After POP Temp_Dict_k_ip")
print(Temp_Dict_k_ip)

fullpath='/home/khayat/Test_New_Auto/Dict_IPs.json'

Dict_all_IP_Usr_Pass_Ena={"a":{"odd":1,"even": 2},"b" :{"odd":3 ,"even": 4},"c":{"odd":5,"even": 6},"d":{"odd":7,"even": 8},"s":{"odd":9,"even": 10}}

data=json.dumps(Dict_all_IP_Usr_Pass_Ena)
with open(fullpath, 'a') as convert_file:
	convert_file.write(data)
os.chmod(fullpath, 0o777)  ## to use it with full permisson
convert_file.close()

Temp_Dict_fake={"h":{'odd':33 ,'even':66}}
# Temp_Dict_fake= {'a':{'odd':333 ,'even':666}}
Temp_Dict_fake_Key= [*Temp_Dict_fake.keys()]




with open(fullpath) as convert_file:
	data=convert_file.read()
convert_file.close()
os.chmod(fullpath, 0o777)  ## to use it with full permisson
data=json.loads(data)
print("Dict:", data)
print("Type:", type(data))

if not Temp_Dict_fake_Key[0] in Dict_all_IP_Usr_Pass_Ena.keys():
	print("A new Key ")
	print("Temp_Dict_fake.keys()")
	print(Temp_Dict_fake.keys())

	data=json.dumps(Temp_Dict_fake)
	with open(fullpath, 'a') as convert_file:
		convert_file.write(data)
	os.chmod(fullpath, 0o777)  ## to use it with full permisson
	convert_file.close()

else :
	print("An old Key ")



# # Print the data of dictionary
# print("\nPeople1:", data['a'])
# print("\nPeople2:", data['b'])
# # Append_to_Old_File(fullpath,)
