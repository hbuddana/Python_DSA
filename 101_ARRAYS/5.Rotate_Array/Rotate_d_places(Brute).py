arr = [1,2,3,4,5]
d=2

main_array = []
rotating_array = []

for i in range(d):
    rotating_array.append(arr[i])

for i in range(d,len(arr)):
    main_array.append(arr[i])

rotated_array = main_array + rotating_array

print("Final Array",rotated_array)
print("elements moving",rotating_array)
print("main elments",main_array)

""""
The time complexity of the code is O(n), where n is the length of the array. This is because the code iterates over the entire array twice, once to copy the first d elements to the rotating_array and once to copy the remaining n-d elements to the main_array.

The space complexity of the code is O(d), where d is the number of rotations. This is because the code uses two auxiliary arrays, rotating_array and main_array, which are both of size d."""