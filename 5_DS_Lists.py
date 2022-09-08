#Initialize two lists and third an empty list
a=[1,2,3,4,5]
b=[2,2,0,2,2]
c=[]
print("list 1 = ", a)
print("list 2 = ", b)

#multiplying two lists and displaying the result

print("Multiplication of lists")
for i,j in zip(a,b):
    print(i, "*", j, " = ", i*j)
    c.append(i*j)
print("Resultant list = ",c)

#Perform max(),min(),sorted(),reverse() on the list

print("Max = ", max(c))
print("Min = ", min(c))
print("Sorted list = ", sorted(c))
c.reverse()
print("Reversed list = ", c)

#Listing the positive numbers in the list and its count

positives=[x for x in c if x>0]
print("no.of.positive numbers = ", positives)
 
