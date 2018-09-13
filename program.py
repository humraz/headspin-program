def palindrome(num):
	
	num=str(num)
	a=list(num)
	a.reverse()
	b=0
	for i in a:
		b=b*10+int(i)
	
	if b==int(num):
		print "it is a palindrome"
	else:
		print "it is not a palindrome"
	


def listofdigits(num):
	print list(str(num))



def series(num):
	print "sum is "	
	i=1
	tot=1.0
	for i in range(3,num+1,2):
		i=float(i)
		
		tot=tot+1/i
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







		
	


