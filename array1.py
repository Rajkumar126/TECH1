n=int(input("enter the size of array:"))
l1=[]
for i in range(n):
    j=int(input("enter the numbers:"))
    l1.append(j)
while(1):
    c=0
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.sort")
    print("5.display")
    print("6.exit")
    print("\n")
    o=int(input("enter the operation you want to perform:"))
    print("\n")
    if(o==1):
        n1=int(input("enter element to insert:"))
        l1.append(n1)
    if(o==2):
        l1.pop()
        print("element deleted successfully")
    if(0==3):
        e=int(input("enter element to search"))
        for i in l1:
            if i==e:
                c=1
        if c==1:
            print("element found")
        if c==0:
            print("element not found")
    if(o==4):
        l1.sort()
    if(o==5):
        for i in l1:
            print(i,end=" ")
    print("\n")
    if(o==6):
        break
    if(o>6):
        print("invalid choice")
