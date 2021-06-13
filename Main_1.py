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

# num=[["a",1,2],["b",3,4],["c",5,6],["d",7,8],["s",9,10]]
# n="n"
# x=[]
# y=[]
# for i in num :
# 	print(i)
# 	x.append(i[0])
		
# print(x)
# for q in num :
# 	for w in q :
# 		if n not in w :
# 			print("False")
# 			y.append(n,m,o)
# print ("y")
# print (y)

# current_date = datetime.date.today().strftime("%y-%m-%d")
# print (current_date)
# print (type(current_date))
