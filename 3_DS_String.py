#String manipulation program

str1=input("Enter a string: ")
str2=" is your string"
print(format('.','.<70'))

#concatenation

print(str1+str2)

#using len(),.upper(),.lower(),.isalpha(),.min(),.max(),.split() on the string
#and slicing the string

print("Length of the string = ",len(str1))
print("Input string in lowercase = ",str1.lower())
print("Input string in uppercase = ",str1.upper())
print("Min of input string = ",min(str1))
print("Max of input string = ",max(str1))
print("slicing the first and last character of input string = ",str1[1:-1])
print("Does the string have only alphabets? ",str1.isalpha())
print("Splitting the input string if seperated by space: ",str1.split())
print(format('.','.<70'))

