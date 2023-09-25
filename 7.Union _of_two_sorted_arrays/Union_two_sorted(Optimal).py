def find_union(arr1, arr2):
    union = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            # If both elements are equal, add one of them to the union
            union.append(arr1[i])
            i += 1
            j += 1

    # Add the remaining elements from both arrays, if any
    while i < len(arr1):
        union.append(arr1[i])
        i += 1

    while j < len(arr2):
        union.append(arr2[j])
        j += 1

    return union
