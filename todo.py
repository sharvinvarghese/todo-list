class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
 
obj=check()
 
choice=1
while choice!=0:
    
    print("0. Exit to-do helper ")

    print("1. Add a task")

    print("2. Delete a task")

    print("3. list task")

    
    choice=int(input("Enter choice: "))
    if choice==1:
        n=str(input("Enter task to add: "))
        obj.add(n)
        print("added ",n)
        
    elif choice==2:
        n=str(input("Enter task to delete: "))
        obj.remove(n)
        print("removed ",n)
        
 
    elif choice==3:
        print("List: ",obj.dis())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()
print(n)