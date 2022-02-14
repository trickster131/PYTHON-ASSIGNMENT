#<<<<<QUESTION 1>>>>>

print('\n\n<<<<<QUESTION1>>>>>\n')
str=input('ENTER A STRING: ')
#Defining a function when word count is more than 1
def word_count(str):
    occurences = dict()
    words = str.split()

    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1

    return occurences
#Counting number of words in string
totalwords=len(str.split())

if totalwords==1:
    frequency = {}
    #Using for loop when word count is 1
    for i in str:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print ("Count of all characters in string is :\n "
                                        +  str(frequency))
else:
    print("Count of all words in string is :\n ",word_count(str)) 

# <<<<<QUESTION 2>>>>>

# A PYTHON PROGRAM TO PRINT NEXT DATE OF INPUT DATE

print('\n\n<<<<<QUESTION2>>>>>\n')
print('A PYTHON PROGRAM TO PRINT NEXT DATE OF INPUT DATE \n')
day=int(input('ENTER DAY: '))
month=int(input('ENTER MONTH: '))
year=int(input('ENTER YEAR: '))
if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025:    

# FOR MONTHS CONTAINING 31 DAYS  

    if month in (1,3,5,7,8,10,12):
        if day<31:
            day=day+1
            year=year
            print('The next day is ',day,'/',month,'/',year)    
        elif day==31:
            #HERE 31ST DECEMBER IS A SPECIAL CASE
            if month==12:
                year=year+1
                print('The next day is 1 / 1/',year)
            else:
                month=month+1
                print('The next day is 1 /',month,'/',year)
        else:
            print('INVALID INPUT')

# FOR MONTHS CONTAINING 30 DAYS.

    elif month in (4,6,9,11):
        if day<30:
            day=day+1
            year=year
            print('The next day is ',day,'/',month,'/',year)
        elif day==30:
            month=month+1
            print('The next day is 1 /',month,'/',year)
        else:
            print('INVALID INPUT')

# SINCE THE DAYS IN FEBRUARY VARIES IN LEAP YEAR, WE APPLY DIFFERENT CONDITIONS FOR IT.   
         
    elif month==2:
        if year%4==0:
            if day<29:
                day=day+1
                print('The next day is ',day,'/',month,'/',year)
            elif day==29:
                month=month+1
                print('The next day is 1 /',month,'/',year)
            else:
                print('INVALID INPUT')
        else:
            if day<28:
                day=day+1
                print('The next day is ',day,'/',month,'/',year)
            if day==28:
                month=month+1
                print('The next day is 1 /',month,'/',year)
            else:
                print('INVALID INPUT')          
else:
    print('INVALID INPUT')

#<<<<<QUESTION3>>>>>

print('\n\n<<<<<QUESTION3>>>>>\n')
list = []
# Taking input for number of elements in list
elements = int(input('Enter number of elements in list:'))
# Using for loop for taking input of elements of list
for i in range(0, elements):
    num = int(input('Enter a number :'))
    y = num, num*num
    # Adding the element and its square to the list
    list.append(y)
# Printing the final list
print(list)


# <<<<<QUESTION 4>>>>>

print('\n\n<<<<<QUESTION4>>>>>\n')
gradepoint=int(input('ENTER YOUR GRADE POINT: '))

# HERE, WE USE DICTIONARIES TO STORE THE TRAITS OF SPECIFIC GRADE POINT

grade={4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',
10:'Outstanding'}

if gradepoint<4 or gradepoint>10:
    print('ERROR')
    quit()
else:
    print('Your Grade is',grade[gradepoint],'and', performance[gradepoint], 'Performance.')

# <<<<<QUESTION 5>>>>>

print('\n\n<<<<<QUESTION5>>>>>\n')
string='ABCDEFGHIJK'
i=11
while(i>0):
    #HERE THE SPACE KEEPS INCREASING BY 1 AND STRING LENGTH KEEPS DECREASING BY 2
    print(' '*int((11-i)/2), string[0:i])
    i=i-2

# <<<<<QUESTION 6>>>>>

print('\n\n<<<<<QUESTION6>>>>>\n')
dictionary= {}

# USING WHILE LOOP TO ADD VALUE IN DICTIONARY
while True:
    name = input('ENTER STUDENT\'s NAME : ')
    sid = input('ENTER STUDENT\'S SID : ')
    choice = input('DO YOU WANT TO ADD ANOTHER VALUE (Y/N) : ')
    # Putting sid as key and student name as value
    dictionary[sid] = name
    # Using while loop to get a valid input
    while choice not in ('Y', 'N'):
        choice= input('DO YOU WANT TO ADD ANOTHER VALUE (Y/N) : ')
    if choice == 'N':
        break

# Printing the dictionary
print(dictionary)

# Sorting dictionary using student name
d1=sorted(dictionary.items(), key=lambda item: item[1])
print(d1)

# Sorting dictionary using sid
d2=sorted(dictionary.items(), key=lambda item: item[0])
print(d2)

# Taking input from user for a student's sid and then printing his/her name
info =(input('ENTER SID OF REQUIRED STUDENT: '))
print('NAME OF STUDENT: ', dictionary.get(info) )    
    
#<<<<<QUESTION 7>>>>>
    
# Write a python program to print Fibonacci sequence also print average of the resultant Fibonacci series

print('\n\n<<<<<QUESTION7>>>>>\n')
Number=int(input("How many terms are to be printed in fibonacci series?\n"))

NUM1 = 0   
NUM2 = 1

if Number<=0:
    print("Please Enter a postive number")

else:
    # Make an empty list
    list=[]                     
    for i in range (0,Number-1):
        if i==0:
            #entering '0' as first term in list
            list.append(NUM1)    
        if i==1:
            #entering '1' as second term in list
            list.append(NUM2)    
            continue
        sum = NUM1+ NUM2
        NUM1 = NUM2
        NUM2 = sum
        #entering the remaining terms
        list.append(sum)        
        sum+=sum

    print("The Required Fibonacci series is:\n",list , "\n")

    #calculating sum of all terms present in list
    sum=0
    for items in list:
        sum = sum + items
    #calculating average
    #len(list)=no. of elements in list    
    Average = sum/len(list)         
    print("Average of following series is:\n",Average , "\n")

    
#<<<<<QUESTION 8>>>>>

print('\n\n <<<<QUESTION 8>>>>')
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

# A new set of all elements that are in Set1 and Set2 but not both.
set4=set1^set2
print(set4)

# A new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
set5=set1^set2^set3
print(set5)

# A new set of elements that are exactly two of the sets Set1, Set2 and Set3.
set6=set1.intersection(set2).union(set2.intersection(set3)).union(set3.intersection(set1))
print(set6)

# A new set of all integers in the range 1 to 10 that are not in Set1.
intset={1,2,3,4,5,6,7,8,9,10}
set7=intset.difference(set1)
print(set7)
    
# A new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
set8=intset.difference(set1.union(set2.union(set3)))
print(set8)    
