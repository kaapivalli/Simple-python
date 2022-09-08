#Library Management System - Exanmple for Object creation and usage

class Library:
    def __init__(self):
        self.book_name=""
        self.author=""
    def getdata(self):
        self.book_name = input("Enter Name of the Book: ")
        self.author = input("Enter Author of the Book: ")
    def display(self):
        print("\n","Name of the Book: ",self.book_name)
        print("Author of the Book: ",self.author)
        print("\n")
books=[]
ch='y'
while(ch=='y'):
    print("PRESS \n 1.ADD NEW BOOK \n 2. DISPLAY BOOKS")
    option=int(input("Enter your choice: "))
    if option==1:
        L = Library()
        L.getdata()
        books.append(L)
    elif option==2:
        for b in books:
            b.display()
    else:
        print("Invalid input")
    ch = input("Press y if you want to continue....")

    
            

            
                            
