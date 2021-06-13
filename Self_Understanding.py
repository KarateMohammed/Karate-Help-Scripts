

def Sec_Fun():
	print("Sec Func")

Sec_name="Sec_name"

class Sec_Student:
	"""docstring for ClassName"""
	def __init__(self, name ="Sec_name", course="Sec_course"):
		self.name=name
		self.course= course	

	def PPrint(self ) :
		print (self.name , self.course)		

class Sec_Student2:
	course="Hey it's class course Global"
	def __init__( self ,name ="Sec_name2_Init", course="Sec_course2_Init",test="Sec_test2_Init") :
		self.test=test
		self.name=name
		print (name , course)

	def PPrint(self ,name ="Sec_name2", course="Sec_course2", test2="Sec_test2") :
		self.test2="Sec_test_in_Func_PPrint "
		course=self.course  # global course
		print (name ,course,test2)

	def PPrint3(self ,name ="Sec_name3", course="Sec_course3",test3="Sec_test3"):
		self.name=name
		self.course=self.course ## global Course 
		self.test3=self.test 	## test under initiate 
		print("PPrint3" ,name,course,test3)  ## use default or Given variables 
		print("PPrint3 with self ",name,self.course,self.test3)  ## use variables from Initiate 


class Variables:
	name ="Mohamed"
	def __init__(
		self,
		name=name,
		course="Sec_course"):
		
		self.name=name
		self.course= course	



if __name__ == '__main__':
	print ("Sec_1_Main")
	Var=Variables()
	print(Var.name ,Var.course)
	Var.name="OUT"
	print(Var.name ,Var.course)
	# Main_Student2=Sec_Student2()
	# Main_Student3=Sec_Student2(test="let's test")

	# print("")
	# print("	Main_Student2.PPrint()")
	# Main_Student2.PPrint()
	# print("")
	# print("	Main_Student3.PPrint()")
	# Main_Student3.PPrint()

	# print("")
	# print("Main_Student2.PPrint(name,Course,test)")
	# Main_Student2.PPrint("name","Course","test")
	# print("")
	# print("Main_Student2.PPrint(name =name_2,Course =Course_2,test2 =test_2)")
	# Main_Student2.PPrint(name="name_2",course="Course_2",test2="test_2")

	# print("")
	# print("#	Main_Student2.PPrint3()")
	# Main_Student2.PPrint3()
	# print("")
	# print("#	Main_Student3.PPrint3()")
	# Main_Student3.PPrint3()
	# print("")
	# print("#	Main_Student3.PPrint3(1,2,3)")
	# Main_Student3.PPrint3(1,2,3)




if not __name__ =='__main__' :
	print ("Sec_1 not run directly")
	Sec_Fun()

