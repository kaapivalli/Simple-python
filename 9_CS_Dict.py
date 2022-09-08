#Get values from user and store it, later to find its sum

size=int(input("enter the number of values: "))
Dic={}
for i in range(size):
    x=int(input("enter element: "))
    Dic.update([(chr(65+i),x)])
print(" The dictionary = ",Dic)
print(" The sum of all values in dictionary = ", sum(Dic.values()))

