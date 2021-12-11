def list_max(input_list):
    max_val = input_list[0]

    for i in range(1, len(input_list), 1):
        if(input_list[i] > max_val):
            max_val = input_list[i]

    return max_val


list1 = [-2, 1, 2, -10, 22, -10]

max_val = list_max(list1)

print(max_val)
