"""volume of a sphere"""
def vol(rad):
    return (4/3)*3.142*(rad**3)

vol(3)

"""Random number check"""
def ran_check(num,low,high):
    for i in range(low,high):
        if num in range(low,high):
            print("THe number is in the range")
    else:
        print("Does not exist in the range")
        
ran_check(2,3,10)
"""Boolean random number check"""
def ran_check(num,low,high):
    for i in range(low,high):
        if num in range(low,high):
            print(True)
    else:
        print(False)
        
ran_check(2,3,10)

"""Number of upper and lowercase characters in a string"""
def up_low(s):
    d={"upper":0, "lower":0}
    for i in s:
        if i.isupper():
            d["upper"]+=1
        elif i.islower():
            d["lower"]+=1
        else:
            pass
    print("Original string : ",s)
    print("number of lower case characters: ",d["lower"])
    print("number of uppercase characters is: ", d["upper"])
                
up_low("My Name is Daniel")

"""Creating A uniqe List"""
def unique_list(l):
    a= []
    for i in l:
        if i not in a:
            a.append(i)
    return a
    
unique_list([1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5])   

"""Multiplying the numbers in a list"""
def multiply(numbers):
    for i in numbers:
        return numbers[0]*numbers[1]*numbers[2]*numbers[3]
    
multiply([1,2,3,-4])

"""Multiplying the numbers in a list """
def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total

multiply([1,2,3,-4])

""" Creating a Palindrome"""
def palindrome(s):
    if s[::-1] == s:
            print(True)
    else:
        print(False)
        
palindrome("omo")

"""Creating a ispangram"""
import string
def ispangram(str1,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

ispangram("The quick brown fox jumps over the lazy dog")

    