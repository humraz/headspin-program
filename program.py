def palindrome(num):
	
	check=num
	c=0
	n=0
	while((num)!=0):
		
		a=num%10
		n=n*10+a
		num=num/10

	if check==n:
		print "it is a palindrome"
	else:
		print "it is not a palindrome"
		
		
	
	
	


def listofdigits(num):
	ls=[]
	while(num!=0):
		a=num%10
		ls.append(a)
		num=num/10

	print ls[::-1]



def series(num):
	print "sum is "	
	i=1.0
	tot=1.0
	for i in range(3,num+1,2):
		tot=tot+1/float(i)
	print tot
		




print "Enter option \n1.To Check palindrome     \n2.Take a number and return a list of its digits    \n3.To find the sum of the series"
print "\nENTER 0 TO EXIT"
val=1
while(val!=0):
	val = int(input())
	if val==0:
		quit()
	print "enter a number"
	num=int(input())
	if val==1:
		palindrome(num)

	if val==2:
		listofdigits(num)

	if val==3:
		series(num)
	
	
	
	print "\nEnter option 1. To Check palindrome     2.Take a number and return a list of its digits    3.To find the sum of the series"







		
	


