def find_max_duplicate(arr):
    arr.sort()

    max_duplicate = None
    prev_num = None
    count = 1
    for num in arr:
        if num == prev_num:
            count += 1
            if count > 1 and (max_duplicate is None or num > max_duplicate):
                max_duplicate = num
        else:
            prev_num = num
            count = 1

    return max_duplicate

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_duplicate = find_max_duplicate(arr)
print("The maximum of the numbers that appear more than once in", arr, "is", max_duplicate)