#Program for dictionary manipulations

keys=[]
print("enter list of 5 keys:")

# getting the keys of dictionary
for i in range(5):
    keys.append(input(f'enter key {i+1}: '))
    
# creating a list of values for each key
vals=[x for x in range(1,6)]

# creating a dictionary with zip()
Dic=dict(zip(keys,vals))

print("The created dictionary => ", Dic)
#-------------------------------
print("Updating the dictionary","*"*10)

#getting a new key value to add to the dictionary
upd_key=input("enter a new key to add: ")
# setting the value of new key
Dic[upd_key]=6

print("*"*10,"New Dictionary => ",Dic)
#--------------------------------
print("Deleting a key-value pair from the dictionary","*"*10)

#getting a key from theuser to delete it from the dictionary
del_key=input(f"enter a key from: {Dic.keys()} ")

if del_key in Dic.keys():
      del Dic[del_key]
else:
    print("key not found")
#---------------------------------
print("*"*10,"\n Final dictionary => ",Dic)


