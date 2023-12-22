import string
#n=input("Enter n\t")
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

upper = string.ascii_uppercase
lower = string.ascii_lowercase
upper_start = ord(upper[0])
lower_start = ord(lower[0])
print(upper_start)
def split(word):
    return [char for char in word]
str=input("Enter a string \n")
n=int(input("Enter the value of n for ROT\t"))
list=[]
assciList=[]
answerList=[]

list=(split(str))
for i in list:
	assciList.append(ord(i))

result=[]
for temp in list:
	if temp in upper:
		result.append(chr(65 + (ord(temp) - 65 + n) % 26))

	elif temp in lower:
		result.append(chr(97 + (ord(temp) - 97 + n) % 26))


	else:
		result.append(temp)


final=listToString(result)

print(final)
