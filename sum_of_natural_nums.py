def sum_of_natural_nums(num):
    # Base Case 
    if num == 0:
        return 0
    else:
        return num + sum_of_natural_nums(num - 1)

print(sum_of_natural_nums(10))