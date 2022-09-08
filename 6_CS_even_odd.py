size=int(input("Enter the size of the array: "))
lis=[]
count_odd = 0
count_even = 0
for i in range(size):
    lis.append(int(input("Enter element {}: ".format(i+1))))

for i in lis:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1

print("Number of odd elements = ",count_odd)
print("Number of even elements = ",count_even)

