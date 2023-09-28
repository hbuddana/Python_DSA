
arr = [1,1,0,1,1,1,1]

maxi = 0
count = 0 

for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
        
    else:
        count = 0

    maxi = max(count,maxi)
    
print(maxi)



