import re
import keyword

print("Enter 5 strings one by one to know if each is a valid python identifier...")

# Initialize necessary variables

string=[]
regex = '^[A-Za-z_][A-Za-z0-9_]*'

#Get five strings from user and append it in a list

for i in range(5):
    string.append(input(f"enter a string {i+1} to check : "))

#traverse the list
print("........................................................")
for i in string:

    if ' ' in i:
        print(i," has space(s), so it is an invalid python identifier")
    # firstly check if the string is a keyword, if yes then print 'invalid'

    elif keyword.iskeyword(i):
        print(i," is an invalid python identifier since it is a keyword")

    #check if it is one of the built_in objects/constants/functions, etc.,

    elif i in dir(__builtins__):
        print(i," is in builtins module. This name is not recommended to be used as an identifier in python")

    #check if the pattern for valid identifier is present in the string

    elif re.search(regex,i):
        #only if the pattern is found throughout the string, it is a valid identifier in python, so
        a=re.search(regex,i)
        if a.end()==len(i):
            print(i," is a valid Python Identifier")

            #the below else will catch cases like 'his,name' where we have comma in the middle
        else:
            print(i," is an invalid python identifier")  
    # else it an invalid identifier again
    #the below else will catch cases like '1_class' or'mail@' where we have invalid starting characters and symbols
    else:
        print(i," is an invalid python identifier")


