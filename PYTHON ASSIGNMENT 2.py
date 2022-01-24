
print('PYTHON ASSIGNMENT 2\n')
#<<<<<<<<<<<QUESTION 1>>>>>>>>>>>

print('<<<<<<<<<<<QUESTION 1>>>>>>>>>>>')
str1='Python is a case sensitive language'
#a.
print(len(str1),'\n')
#b.
print(str1[::-1],'\n')
#c.
str2=str1[10:26]
print(str2,'\n')
#d
print(str1.replace('a case sensitive','object oriented'),'\n')
#e
print(str1.index('a'),'\n')
#f
print(str1.replace(' ',''),'\n\n')

#<<<<<<<<<<<QUESTION 2>>>>>>>>>>>

print( '<<<<<<<<<<<QUESTION 2>>>>>>>>>>>\nProgram to store name, SID, department name and CGPA into different variables\n')

NAME= 'VIVEK TIWARI'
SID= '21104037'
DEPARTMENT= 'ELECTRICAL ENGINEERING'
CGPA= '10'
print('Hey,', NAME, 'Here! \n\nMy SID is', SID, '\nI am from', DEPARTMENT, 'department and my CGPA is', CGPA,'\n\n') 

#<<<<<<<<<<<QUESTION 3>>>>>>>>>>>

print('<<<<<<<<<<<QUESTION 3>>>>>>>>>>>')
a=56
b=10
#a.
print('a&b=', a&b)
#b.
print('a|b=', a|b)
#c.
print('a^b=', a^b)
#d
print("a << 2 =", a << 2)
print("b << 2 =", b << 2)
#e
print("a >> 2 =", a >> 2)
print("b >> 4 =", b >> 4,'\n\n')

#<<<<<<<<<<<QUESTION 4>>>>>>>>>>>

print('<<<<<<<<<<<QUESTION 4>>>>>>>>>>>\nA Python program to find the greatest of three numbers entered by the user\n')

num1=int(input('ENTER FIRST NUMBER: '))
num2=int(input('ENTER SECOND NUMBER: '))
num3=int(input('ENTER THIRD NUMBER: '))
if num1>num2 and num1>num3:
    print(num1, 'is greatest') 
elif num2>num1 and num2>num3:
    print(num2, 'is greatest')
else:
    print(num3, 'is greatest')
print('\n\n')

#<<<<<<<<<<<QUESTION 5>>>>>>>>>>

print('<<<<<<<<<<<QUESTION 5>>>>>>>>>>>\nProgram to check if the word “name” is present in the string entered by the user\n')

str=input('ENTER YOUR STRING: ')
print('YES') if 'name' in str else print('NO')
print('\n\n')

#<<<<<<<<<<<QUESTION 6>>>>>>>>>>>

print('<<<<<<<<<<<QUESTION 6>>>>>>>>>>>\nProgram to check whether a triangle can be formed or not\n')

SIDE1=int(input('ENTER FIRST SIDE LENGTH: '))
SIDE2=int(input('ENTER SECOND SIDE LENGTH: '))
SIDE3=int(input('ENTER THIRD SIDE LENGTH: '))
if SIDE1>SIDE2+SIDE3:
    print('NO TRIANGLE CANNOT BE FORMED')  
elif SIDE2>SIDE1+SIDE3:
    print('NO TRIANGLE CANNOT BE FORMED') 
elif SIDE3>SIDE2+SIDE1:
    print('NO TRIANGLE CANNOT BE FORMED')     
else:
    print('YES TRIANGLE CAN BE FORMED')

        
