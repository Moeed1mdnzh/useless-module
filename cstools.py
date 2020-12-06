#####################
#COMPLEX STRING TOOLS
#####################
from Error import *
import random
import numpy as np
import random as r

class String:
	###Functions that are useful in different cases and python doesn't include them
	def __init__(self):
		self.emp_s = ''
		self.upc = "UPPER"
		self.lwc = "LOWER"
	def replace(self,string,index,c,start=0,end=None):
		#Python's replace function replaces all the same strings with one string but here it replaces a specific string
		"""
		string : a specific string
		index : the index of the character that we want to remove it and replace it with another character
		c : the character that is going to be in our new string
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		self.emp_s = ''
		string = string[start:end]
		for i,n in enumerate(string):
			if i != index:
				self.emp_s += n
			if i == index:
				self.emp_s += c
		return self.emp_s
	def shuffle(self,string,start=0,end=None):
		#Shuffles a string randomly
		"""
		string : a specific string
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = self.aspace(string,start,end)
		string = string.split()
		random.shuffle(string)
		return ''.join(string)
	def place(self,*args):
		#Takes strings of the same length and extends string1 first element with string2 first element ..... until n element
		"""
		*args : specific strings with the same length
		"""
		self.emp_s = ''
		try:
			for i in range(len(args[0])):
				for s in range(len(args)):
					self.emp_s += args[s][i]
		except IndexError:
			raise ReachedlimitError("[ERROR] : All strings should have the same length.")
		return self.emp_s
	def extend(self,*args):
		#Connects several strings together
		"""
		*args : specific strings, length doesn't matter here
		"""
		self.emp_s = ''
		for i in range(len(args)):
			self.emp_s += args[i]
		return self.emp_s
	def rspace(self,string,start=0,end=None):
		#Removes spaces between strings
		"""
		string : a specfic string
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		return ''.join(string.split())
	def aspace(self,string,start=0,end=None):
		#Adds spaces between strings
		"""
		string : a specific string
		start : starting point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		self.emp_s = ''
		for n in string:
			self.emp_s += n
			self.emp_s += ' '
		return self.emp_s
	def subtr(self,string1,string2):
		#Removes strings from string1 as long as the length of the string2 
		"""
		string1 : the string that is going to be subtracted by another string
		string2 : the second string
		"""
		self.emp_s = ''
		self.emp_s = string1[len(string2):]
		return self.emp_s
	def revrs(self,string,start=0,end=None):
		#Reverses a string
		"""
		string : the string that is going to be reversed
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		return string[::-1]
	def case(self,string,U_L,start=0,end=None):
		#Converts a string to uppercase and lowercase
		"""
		string : a specific string
		U_L : the argument that defines if the string should be converted to uppercase or lowercase.
		to define it just write cstools.String().upc or cstools.String().lwc
		start : starting point
		end = ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		if U_L == self.lwc:
			if string.islower():
				raise CaseError("[ERROR] : The whole string is in lowercase.")
			else:
				return string.lower()
		if U_L == self.upc:
			if string.isupper():
				raise CaseError("[ERROR] : The whole string is in uppercase.")
			else:
				return string.upper()
		else:
			raise WrongArgumentError("[ERROR] : Invalid argument for 'U_L' parameter.\nShould be cstools.String().upc or cstools.String().lwc")
####################
class Tools:
	###Math in strings
	def __init__(self,emp_l=[]):
		self.emp_l = emp_l
	def add(self,string,num,start=0,end=None):
		#Adds string to itself for specific times
		"""
		string : a specific string
		num : the times that the string is going to be added by itself
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		for i in range(num):
			string += string[0]
		string = string[0:-1]
		return string
	def sub(self,string,num,start=0,end=None):
		#Subtracts elements in a string for specific times
		"""
		string : a specifc string
		num : the times that the string is going to lose characters
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)

		string = string[start:end]
		for i in range(num):
			string = string[0:len(string)-1]
		if string == '':
			return None
		return string
	def mul(self,string,num,start=0,end=None):
		#Multiplies the string by itself for specific times
		"""
		string : a specific string
		num : the times that the string is going to be multiplied by itself
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		if num > 20:
			raise ReachedlimitError(f"[ERROR] : Take a lower number than 21. [YOUR NUMBER] : {num}\nThis is going to cause a MemoryError.")
		for i in range(num):
			string += string
		return string
	def divide_parts(self,string,division_num,start=0,end=None):
		#Divides string to specific parts
		"""
		string : a specific string
		division_num : number of the parts that the string is going to be splited to
		start : starting point
		end : ending point
		"""
		self.emp_l = []
		head = 0
		d = division_num
		if end == None:
			end = len(string)
		string = string[start:end]
		while division_num <= len(string):
			self.emp_l.append(string[head:division_num])
			head += d
			division_num += d
		return self.emp_l
	def pow(self,string,num,start=0,end=None):
		#Powers string for specifc times
		"""
		string : a specific string
		num : times that the string is going to be powered by itself
		start : starting point
		end : ending point
		"""
		if end == None:
			end = len(string)
		string = string[start:end]
		if num > 7:
			raise ReachedlimitError(f"[ERROR] : Take a lower number than 8. [YOUR NUMBER] : {num}\nThis is going to cause a MemoryError.")
		for i in range(num):
			string *= num
		return string
	def divide(self,string1,string2,start=0,end=None):
		#Divides string1 by string2, Example : string1 = "hhhh" string2 = "h"  result will be 4 
		"""
		string1 : a specific string that all the characters are the same
		string2 : one character from string1
		"""
		if end == None:
			end = len(string1)
		string1 = string1[start:end]
		for i in range(999999):
			if string2*i == string1:
				return i
####################
class Generate:
	#Generates different strings
	def __init__(self):
		self.emp_s = ''
		self.sP = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1',
		 '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 
		'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

		self.cP = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
		 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
		  'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '`', '!', '#', '$', '%', '^',
		 '&', '*', '(', ')', '-', '_', '[', ']', '{', '.', '/', '}', '|', "'", ',', '<', '>', ';', ':']
		self.space = ' '
		self.count = 0
		#"pwɘɿƚyuioqɒƨbʇǫʜႱʞlzxɔvdnm"
		self.mirror_words = {"q":"p","w":"w","e":"ɘ","r":"ɿ","t":"ƚ","y":"y","u":"u","i":"i","o":"o","p":"q",
		"a":"ɒ","s":"ƨ","d":"b",
		"f":"ʇ","g":"ǫ","h":"ʜ","j":"Ⴑ","k":"ʞ","l":"l","z":"z","x":"x","c":"ɔ","v":"v","b":"d","n":"n","m":"m"}
		self.replacer = String().replace
	def snake(self,string,roll=4,start=0,end=None):
		#Generates a sting snake and rolls for specific times
		"""
		string : a specific string
		roll : times that the string should roll
		start : starting point
		end : ending point
		"""
		end = self.check(end,string)
		string = string[start:end]
		for i in range(roll):
			while self.count <= 40:
				print(self.space + string)
				self.space += ' '
				self.count += 1
			while self.count >= 1:
				self.space = self.replacer(self.space,0,'')
				print(self.space + string)
				self.count -= 1
			self.count = 0
			self.space = ' '
	def matrix1D(self,string,size,start=0,end=None):
		#Generates a 1D matrix of specific string
		"""
		string : a specific string
		size : length of the matrix, should be an integer
		start : starting point
		end : ending point
		"""
		try:
			end = self.check(end,string)
			string = string[start:end]
			if type(size) != int:
				raise Error.WrongArgumentError("[ERROR] : Invalid argument for 'size' parameter.\n Expected an integer.")
			end = self.check(end,string)
			string = string[start:end]
			return np.full(size,string)
		except MemoryError:
			raise ReachedlimitError(f"[ERROR] : An 'MemoryError' occured.\n You don't have enough space to create an array with shape {size}.")
	def matrix2D(self,string,size,start=0,end=None):
		#Generates a 2D matrix of specific string
		"""
		string : a specifc string
		size : the dimensions of the matrix. n x n
		start : starting point
		end : ending point
		"""
		try:
			end = self.check(end,string)
			string = string[start:end]
			if len(size) > 2 or len(size) < 2:
				raise WrongArgumentError("[ERROR] : Invalid argument for 'size' parameter.\n Expected an 2D tuple.")
			end = self.check(end,string)
			string = string[start:end]
			return np.full(size,string)
		except MemoryError:
			raise ReachedlimitError(f"[ERROR] : An 'MemoryError' occured.\n You don't have enough space to create an array with shape {size}.")
	def matrix3D(self,string,size,start=0,end=None):
		#Generates a 3D or higher matrix of specifc string
		"""
		string : a specific string
		size : the dimensions of the matrix. n x n x n or higher
		"""
		try:
			end = self.check(end,string)
			string = string[start:end]
			if len(size) < 3:
				raise WrongArgumentError("[ERROR] : Invalid argument for 'size' parameter.\n Expected an 3D or higher dimension size as a tuple.")
			end = self.check(end,string)
			string = string[start:end]
			return np.full(size,string)
		except MemoryError:
			raise ReachedlimitError(f"[ERROR] : An 'MemoryError' occured.\n You don't have enough space to create an array with shape {size}.")
	def password(self,filter=[]):
		self.__init__()
		#Generates a random password
		"""
		filter : characters that shouldn't be in the password
		"""
		self.emp_s = ''
		if filter != []:
			for n in filter:
				self.sP.remove(n)
		for i in range(8):
			self.emp_s += r.choice(self.sP)
		return self.emp_s

	def c_password(self,num=8,new=None,filter=[]):
		#Generates a random complex password
		"""
		num : length of the password
		new : new characters to be added to your password
		filter : characters that shouldn't be in the password
		"""
		self.__init__()
		self.emp_s = ''
		if filter != []:
			for n in filter:
				self.cP.remove(n)
		if new != None:
			for n in new:
				self.cP.append(n)
		for i in range(num):
			self.emp_s += r.choice(self.cP)
		return self.emp_s
	def mirror(self,string,start=0,end=None):
		#Converts string to mirror version of it
		"""
		string : a specific string
		start : starting point
		end : ending point
		"""
		end = self.check(end,string)
		string = string[start:end]
		self.emp_s = ''
		for n in string:
			if n.isupper():
				self.emp_s += self.mirror_words[n.lower()].upper()
				continue
			if n not in self.mirror_words:
				self.emp_s += n
				continue
			self.emp_s += self.mirror_words[n]

		return self.emp_s
	def check(self,n,s):
		#Spliting string
		"""
		n : ending point og a string
		s : a specfic string to get the length of it
		"""
		if n == None:return len(s)
		else: return n
####################
class Slt(Generate):
	#SIMPLEX LIST TOOLS
	def __init__(self):
		super().__init__()
		self.result = 0
		self.result_list = []
		self.length = 0
	def add(self,List,start=0,end=None):
		#Adds all elements of a list 
		"""
		List : a specific list
		start : starting point 
		end : ending point
		"""
		self.result = 0
		end = self.check(end,List)
		List = List[start:end]
		for i in range(len(List)):
			self.result += List[i]
		return self.result
	def sub(self,List,start=0,end=None):
		#Subtracts all elements of a list
		"""
		List : a specific list
		start : starting point 
		end : ending point
		"""
		self.result = 0
		end = self.check(end,List)
		List = List[start:end]
		for i in range(len(List)):
			self.result -= List[i]
		return self.result
	def mul(self,List,start=0,end=None):
		#Multiplies all elements of a list
		"""
		List : a specific list
		start : starting point 
		end : ending point
		"""
		self.result = 1
		end = self.check(end,List)
		List = List[start:end]
		for i in range(len(List)):
			self.result *= List[i]
		return self.result
	def divide(self,List,start=0,end=None):
		#Divides all elements of a list
		"""
		List : a specific list
		start : starting point 
		end : ending point
		"""
		self.result = 0
		end = self.check(end,List)
		List = List[start:end]
	def pow(self,List,start=0,end=None):
		#Powers all elements of a list
		"""
		List : a specific list
		start : starting point 
		end : ending point
		"""
		self.result = 0
		end = self.check(end,List)
		List = List[start:end]
	def list_password(self,filter=[],num=5,num2=5):
		#Returns a list of random passwords
		"""
		filter : characters that shouldn't be in the password
		num : length of the list
		num2 : length of each password
		"""
		self.__init__()
		if filter != []:
			for n in filter:
				self.sP.remove(n)
		for i in range(num):
			self.emp_s = ''
			for i in range(num2):
				self.emp_s += r.choice(self.sP)
			self.result_list.append(self.emp_s)
		return self.result_list
	def betw(self,List,start=0,end=None):
		#Finds the middle point
		"""
		List : a specific list
		start : starting point
		end : ending point
		"""
		end = self.check(end,List)
		List = List[start:end]
		self.__init__()
		if len(List) % 2 == 0:
			raise EvenlengthError("[ERROR] : Only lists with odd length can have an element in the middle.\n Example : [1,2,3,4,5] the number is going to be 3.")
		else:
			return List[round(len(List)/2)]
####################			
class Shapes:
	def __init__(self):
		self.space = ""
		self.new_line = ""
		self.divisible_num = 0
		self.clone = None
		self.keep = True
		self.random_strings = []
	def square(self,string,length=10,start=0,end=None):
		#Generates a square of a specific string
		"""
		string : a specific string
		length : length of all sides
		start : starting point
		end : ending point
		"""
		self.__init__()
		end = self.check(end,string)
		string = string[start:end]
		possib_nums = []
		for i in range(1,len(string)):
			if len(string)%i == 0:
				possib_nums.append(i)
		for i in range(max(possib_nums)):
			self.new_line += "\n"
		self.spaces = ''.join([''.join([string+' ' for i in range(length)])+self.new_line for i in range(length)])
		return self.spaces
	def triangle(self,string,side=6,start=0,end=None):
		#Generates a triangle of a specific string
		"""
		string : a specific string
		side : length of each side
		start : starting point
		end : ending point
		"""
		self.__init__()
		end = self.check(end,string)
		string = string[start:end]
		test = string
		if side%2 != 0:
			raise OddsideError(f"[ERROR] : Expected an even number as side.Your number : {side}")
		else:
			for i in range(side):
				for i in range(2):
					for i in range(side//2):
						self.space += " "
					if self.keep:
						self.space += string
						self.keep = False
				self.space += "\n"
				string += test[0]
				string += test[0]
				side -= 2
				self.keep = True
				if side <= 0: 
					return self.space
	def rectangle(self,string,width,height,start=0,end=None):
		#Generates a rectangle of a specific string
		"""
		string : a specific string
		width : length of the width
		height : length of the height
		start : starting point
		end : ending point
		"""
		self.__init__()
		end = self.check(end,string)
		string = string[start:end]
		for i in range(height):
			for j in range(width):
				self.space += string
			self.space += "\n"
		return self.space
	def circle(self,string,start=0,end=None):
		#Generates a circle of a specific string
		"""
		string : a specific string
		start : starting point
		end : ending point
		"""
		end = self.check(end,string)
		string = string[start:end]
		radius = 10
		test = string
		test2 = radius
		Space = "   "
		if radius%2 != 0:
			raise OddsideError(f"[ERROR] : Expected an even number as radius.Your number : {radius}")
		else:
			for i in range(radius):
				self.random_strings.append(string)
				for i in range(2):
					for i in range(radius//2):
						self.space += " "
					if self.keep:
						self.space += string
						self.keep = False
				self.space += "\n"
				for i in range(2):
					string += test[0]
				self.keep = True
				if radius != test2-6:
					radius -= 2
				else:
					if len(string) > 1:
						string = string[:len(string)-2]
					for i in range(2):
						for i in range(radius//2):
							self.space += " "
						if self.keep:
							self.space += string
							self.keep = False
						self.space += "\n"
						self.keep = True
					self.random_strings.remove(self.random_strings[-1])
					self.random_strings = self.random_strings[::-1]
					for i,v in enumerate(self.random_strings):
						self.random_strings[i] = Space + self.random_strings[i]
						Space += " " 
					self.space += ''.join([s+"\n" for s in self.random_strings])
					return self.space	
	def diamond(self,string,side=6,start=0,end=None):
		#Generates a diamond of a specific string
		"""
		string : a specific string
		side : length of all sides
		start : starting point
		end : ending point
		"""
		self.__init__()
		end = self.check(end,string)
		string = string[start:end]
		self.space = self.triangle(string,side)
		self.space = self.space[0:len(self.space)-1]
		self.space += self.triangle(string,side)[::-1]
		return self.space
	def check(self,n,s):
		#Spliting string
		"""
		n : ending point
		s : a string
		"""
		if n == None:return len(s)
		else: return n
