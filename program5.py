b1,b2,b3=input().split()
b1=int(b1)
b2=int(b2)
b3=int(b3)

if(b1 > b2) and (b1 > b3):
    largest =b1
elif(b2 > b1) and (b2 > b3):
    largest=b2
else:
    largest=b3
    
print(largest)    
    
   
