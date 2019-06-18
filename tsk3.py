#!usr/bin/python3

x=[]
y=[]

list_1 = list(map(int,input("Enter the list of numbers with spaces in between : ").split()))


for i in list_1:
    if i > 5:
        x.append(i)
    if i <= 2:
        y.append(i)

print("Numbers greater than five : ", x)
print("Numbers less than equal to two : ", y)

