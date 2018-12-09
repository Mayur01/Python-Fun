print("Enter list of number seperated by space:")
list = [int(x) for x in input().split()]
m= 0
print(list)
for i in list:
    if i > m:
        m=i
print("The maximum number is ",m)
