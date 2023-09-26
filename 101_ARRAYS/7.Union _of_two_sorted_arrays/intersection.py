def find_intersection(arr1, arr2):
    intersection = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            # If both elements are equal, add one of them to the intersection
            intersection.append(arr1[i])
            i += 1
            j += 1

    return intersection


arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(find_intersection(arr1, arr2))