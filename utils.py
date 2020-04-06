def find_max(find_from_list):
    largest_number = find_from_list[0]
    for i in find_from_list:
        if i > largest_number:
            largest_number = i
    return largest_number
