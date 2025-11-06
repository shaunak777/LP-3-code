def knapsack(w,wt,val,n):
    
    dp=[[0 for x in range(w+1)]for x in range (n+1)]
  
    for i in range(n+1):
           for w in range(w+1):
            if i==0 or w==0:
               dp[i][w]=0
            elif wt[i-1]<=w:
                 dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
               dp[i][w]=dp[i-1][w]
        
    return dp[n][w]

n=int(input("Enter number of items:"))
val=[]
wt=[]

for i in range(n):
    val.append(int (input(f"Enter value of item {i+1}:")))
    wt.append(int(input(f"Enter weight of item {i+1}:")))
w=int(input("ENter maximum capacity of Knapsack:"))

max_value=knapsack(w,wt,val,n)
print("Maximum value can be put in knapsack= ",max_value)
