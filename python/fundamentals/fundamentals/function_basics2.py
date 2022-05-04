def countdown(num):
    new_list = []
    for num in range(num, -1, -1):
        new_list.append(num)
    print(new_list)

countdown(5)

def print_return(list_of_nums):
    print(list_of_nums[0])
    return list_of_nums[1]

print_return([2,3])

def first_plus_length(list_of_nums):
    return list_of_nums[0]+len(list_of_nums)

first_plus_length([1,2,3,4,5,6,7,8,9])

def values_greater_than_second(list_of_nums):
    if len(list_of_nums) < 2:
        return False
    list_of_greater_than_second_numbers = []
    for num in list_of_nums:
        if num > list_of_nums[1]:
            list_of_greater_than_second_numbers.append(num)
    print(len(list_of_greater_than_second_numbers))
    return list_of_greater_than_second_numbers

values_greater_than_second([5,2,3,2,1,4,6,5,2,45,2])

def length_value(length, value):
    new_list = []
    for num in range(length):
        new_list.append(value)
    return new_list

length_value(4,7)