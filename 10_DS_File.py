#In your working (current) directory (folder) save a text file called readfile
#write somethong into it and save
#Get a image file in png format, rename it as demo_img and save it also in your
#working directory.
#Finally write and save this python program (.py file) also in the same folder
#for this program to work properly

f1 = open('./readfile.txt','r')
f2=open('./writefile2.txt','w')

info=f1.readlines()
print("contents of first text file are \n", info)
for i in range(len(info)):
    f2.write(info[i])
f1.close()
f2.close()
f2=open('./writefile2.txt','r')
info_2=f2.read()
print("contents of second text file are \n",info_2)
f2.close()
print("contents of binary files...............")
f3=open('./demo_img.png','rb')
byte = f3.read(1)
for i in range(10):
    print(byte)
    byte = f3.read(1)
f3.close()



