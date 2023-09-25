arr = [1,0,2,3,2,0,0,4,5,1]

temp = []
size = len(arr)

# Appends all the Non-Zero numbers to the Temporary array
for i in range(size):
    if(arr[i]!=0):
        temp.append(arr[i])


# No of Zeroes in the main array that need to be added at the new_temp
no_of_zeros = size - len(temp)

#Add the Zeroes at the end
for i in range(0, no_of_zeros):
    temp.append(0)

print(temp)

# Time & Space Complexity - O(n)


