sum_of_huge_number = 0

for integers in range(151):
    print (integers)

for multiple_of_five in range(5, 1001, 5):
    print(multiple_of_five)

for counting_dojo_way in range(1, 101):
    if not counting_dojo_way % 10:
        print("Coding Dojo")
    elif not counting_dojo_way % 5:
        print("Coding")
    else:
        print(counting_dojo_way)

for huge_number in range (0, 500001):
    if huge_number % 2:
        sum_of_huge_number += huge_number

print(sum_of_huge_number)

for countdown in range (2018, 0, -4):
    print(countdown)

low_num = 2
high_num = 9
mult = 3

for low_num in range(low_num, high_num+1):
    if not low_num % mult:
        print (low_num)