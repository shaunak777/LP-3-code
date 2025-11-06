n=int (input("Enter the number of terms:"))
a,b=0,1
steps=0

print("Fibonacci Sequence:")
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
    steps+=1
print("\nTotal steps taken:",steps)    