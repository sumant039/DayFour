#!/usr/bin/python
import sys
#from math import sqrt
#import math
#m is acting as alias of m or object
import math as m
sys.path.insert(1,"/home/gaurav/test")
import customModule as c
#python main lib functions
#join and split

print (sys.path)
str1="hello"
str2="world"
str3=(str1,str2)
#delimter i.e : , - 
str3=":".join(str3)


print str3

str4=(str1,str2,str3)
str5="-".join(str4)
print str5

list1=[]
#server1:192.168.1.12

list1=str3.split(":")

print list1


#map in Python

def addition(n):
    #when we se from math import sqrt
    m.sqrt(n)
    #when using import math
    #math.sqrt(n)

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)

print("map results",list(result))


#lambda function

fun=lambda n: n*n 

print "lambda result",fun(4)

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

#filter in Python

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


#Python Function 

def Function(a,b):
    return a*b

res=Function(2,3)

print("Multilply res is",res)

#list comprehension
list4=[3,5,8,9,10]
newList=[x*x for x in list4]

print newList
sum=c.customFunction(8,9)

print("sum from customModule is",sum)
#Custom module creation

#Extract the ip address from a file ,each line contains format server:ipaddress
#extract the ip address and ping them and check whether the server is available or not.
#Using filter find the vowels in a list of charcaters from a-z
#Using math library and map function  find the exponent of each element of list
#Using Filter function find whether a number is prime or not and print the final list containing All prime numbers
#Join all elements in list with - 




