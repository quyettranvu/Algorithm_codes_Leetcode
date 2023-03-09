def series_lengths_and_values(arr):
    arr.sort()
    
    series_lengths = []
    series_values = []
    
    current_value = None
    current_length = 0
    
    for num in arr:
        if num != current_value:
            if current_value is not None:
                series_lengths.append(current_length)
                series_values.append(current_value)
            # Start a new series
            current_value = num
            current_length = 1
        else:
            current_length += 1
    series_lengths.append(current_length)
    series_values.append(current_value)

    print("Values of elements that form series:", series_lengths)
    print("Lengths of consecutive identical elements:", series_values)
    return (series_lengths, series_values)

series_lengths_and_values([3, 5, 1, 3, 5, 3])