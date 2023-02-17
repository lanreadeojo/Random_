def bubble_sort(num_list):
    '''
    :param num_list: List of numbers
    :return: Sorted list of numbers
    '''
    for i in range (len (num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp


my_list = [4, 266, 9, 24,44,54,41,54,41,89,20]
bubble_sort(my_list)
print(my_list)


