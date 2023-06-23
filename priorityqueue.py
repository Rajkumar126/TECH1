students_qrade=[]
students_qrade.append((1,"Akash"))
students_qrade.append((2,"ankitha"))
students_qrade.sort(reverse=True)
print("yes")
print(students_qrade)
students_qrade.append((3,'sid'))
students_qrade.sort(reverse=True)
print("priority wise sorted")
print(students_qrade)
print("Original queue")
while students_qrade:
    print(students_qrade.pop())