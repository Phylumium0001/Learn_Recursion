def sum_of_natural_nums(num,sum):
    # Base Case 
    if num == 0:
        return sum
    else:
        sum += num
        return sum_of_natural_nums(num-1,sum)
        # return num + sum_of_natural_nums(num - 1)

print(sum_of_natural_nums(10,0))