N=list(map(int,input("Enter a list:").split()))
reversed_list=[]
for i in N:
    reversed_list.insert(0,i)
print("Reversed list is:",reversed_list)