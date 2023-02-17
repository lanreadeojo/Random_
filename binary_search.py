def binary_search(number_list, number):
    '''

    :param number_list:list of numbers
    :param number: number to find
    :return: True if number is found if number is not found
    '''

    first = 0
    last = len(number_list)-1

    number_found = False
    while first <= last and number_found is False:
        middle = int((first + last)/2)
        if  number_list[middle] == number:
            number_found = True

        if number < number_list[middle]:
            last = middle -1
        else:
             first = middle + 1
    return number_found

print (binary_search([1,2,3,4,5,6,7,8,9,10], 3))
