#initialize two lists: one with some values and another empty

t1 = (0, 2, 3, -3, 13, 7, 17, 88, 45, 56)
t2 = ()
print("The Tuple = ", t1)

# Check if the tuple has got any prime numbers
#Print the prime numbers if present and its count

Flag = True
for t in t1:
    if t <= 0 or t == 1:
        continue
    elif t == 2:
        t2 += (t,)
    else:
        for i in range(2,t):
            if t % i == 0:
                Flag = False
        if Flag == True:
            t2 += (t,)
print("Prime numbers in the tuple are = ", t2)
print("No.Of. Prime numbers = ", len(t2))
                

