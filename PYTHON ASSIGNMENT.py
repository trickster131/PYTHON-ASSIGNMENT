#QUESTION 1

num1=input("ENTER THE FIRST NUMBER:")
num2=input("ENTER THE SECOND NUMBER:" )
num3=input("ENTER THE THIRD NUMBER:")
print("THE AVERAGE OF THREE NUMBERS Is ", int((int(num1)+int(num2)+int(num3))/3), "\n" )


#QUESTION 2

GROSS_INCOME=input("ENTER YOUR GROSS INCOME:")
NUMBER_OF_DEPENDANTS=input("ENTER THE NUMBER OF DEPENDANTS:")
#Taxable income = Gross Income - Standard deduction - (Dependent deduction * No. of dependents)
#Tax = Taxable Income * Tax Rate
TAX_RATE=0.2
print("TAX TO BE PAID IS:",int((int(GROSS_INCOME)-10000-(3000* int(NUMBER_OF_DEPENDANTS)))*TAX_RATE),"\n" )


#QUESTION 3

SID=input("ENTER YOUR SID:")
Name=input("ENTER YOUR NAME:")
Gender=input("ENTER YOUR GENDER:")
Course_Name=input("ENTER YOUR COURSE NAME:")
CGPA=input("ENTER YOUR CGPA:")
STUDENT=[SID, Name, Gender, Course_Name, CGPA]
print(STUDENT,"\n")


#QUESTION 4

MARKS_OF_FIRST_STUDENT=input("MARKS OF FIRST STUDENT:")
MARKS_OF_SECOND_STUDENT=input("MARKS OF SECOND STUDENT:")
MARKS_OF_THIRD_STUDENT=input("MARKS OF THIRD STUDENT:")
MARKS_OF_FOURTH_STUDENT=input("MARKS OF FOURTH STUDENT:")
MARKS_OF_FIFTH_STUDENT=input("MARKS OF FIFTH STUDENT:")
MARKS=[MARKS_OF_FIRST_STUDENT,MARKS_OF_FIRST_STUDENT,MARKS_OF_SECOND_STUDENT,MARKS_OF_THIRD_STUDENT,MARKS_OF_FOURTH_STUDENT,MARKS_OF_FIFTH_STUDENT]
MARKS.sort()
print(MARKS,"\n","\n")


#QUESTION 5


# 1ST PART

COLORS=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

COLORS.remove('Black')
print(COLORS,"\n")

# 2ND PART
COLORS=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

COLORS[3]='Purple'
COLORS[4]='Purple'
print(COLORS)
