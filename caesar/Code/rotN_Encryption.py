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
def split(word):
    return [char for char in word]

def rotEncrypt(str,n):
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	list=[]
	assciList=[]
	answerList=[]

	list=(split(str))
	for i in list:
		assciList.append(ord(i))

	result=[]
	for temp in list:
		if temp in upper:
			var=ord(temp)-n
			if var <ord ('A'):
				dif=ord('A')-var
				var=ord('Z')-(dif-1)
		
			result.append(var)
		elif temp in lower:
			var=ord(temp)-n
			if var <ord ('a'):
				dif=ord('a')-var
				var=ord('z')-(dif-1)
			result.append(var)


		else:
			result.append(temp)

	count=0
	answer=[]
	letteranswerlist=[]
	for i in result:
		answer.append(i)
		
	for i in answer:

		try:
			temp=chr(i)
			letteranswerlist.append(temp)
	
		except:
			letteranswerlist.append(i)
	
	return listToString(letteranswerlist)

str=input("Enter a string \n")
n=int(input("Enter the value of n for ROT\t"))
output=rotEncrypt(str,n)
print(output)
