#first code of python
print("My name is mayank")
print("I am learning python")
#python by default break the line in result 


#To remove the break between the lines we can use end parameter in print function
#end = " it will print whatever u write between the double quotes instead of break"

print("my name is mayank", end = " ")
print("I am learning python")
#after running this code u will find that the output of both the print statements will be in same line because we have used end parameter in first print statement

#if we multiplay the string with a number it will print the string that many times
print("my name is mayank" *10)

#if we want to break the line we add \n to the string
print("my name is mayank \n"*100)

#num (it is a variable )
# '=' it is a assignment operator
# it assign values to the variable from right to left  
# which works from right to left 
#why assignment operator works from right to left


#to check the type of variable we can use type() function
A=89.5
print(type(A))

#python support hetrogeneous data types in a single variable
A=89
print(type(A))

B= "jecrc "
print(type(B))

A=836
B=1096
sum= A+B
print("Sum of A and B is ", sum)

num1 = 5 
num2 = 6
print( num1 + num2)

#Rule-> function/method always return the value

#we have to define the type of the data we enter 
#exception in this is Constructor And destructor
#input method return string type of data
A= (input("Enter the value of A: "))
B= (input("Enter the value of B: "))
sum= A+B
print("Sum of A and B is ",sum)



#typecasting is the process of converting one data type into another data type
A= int(input("Enter the value of A: "))
B= int(input("Enter the value of B: "))
sum= A+B
print("Sum of A and B is ",sum)