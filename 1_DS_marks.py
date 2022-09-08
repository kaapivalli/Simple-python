total=0
marks=[]
no_of_subjs=5
for i in range(no_of_subjs):
    x=int(input(f"enter mark of subject {i+1}: "))
    marks.append(x)
    total=total+marks[i]
print("Total marks = ",total)
percentage=(total/500)*100
if percentage>=80:
    print("your grade  is A")
elif 70<=percentage<80:
    print("your grade is B")
elif 60<=percentage<70:
    print("your grade is C")
elif 40<=percentage<60:
    print("your grade is D")
else:
    print("No grade")


