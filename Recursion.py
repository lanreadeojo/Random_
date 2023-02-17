def bottles_of_beer(num_of_beer):
    ''' use recursion to print the bottles of beer song'''
    '''
    :param num_of_beer: Integer number of beers that are on the wall.
    '''
    if num_of_beer < 1:
        print ("No more bottles of beer on the wall. No more bottles of beer")
        return
    curr_num_of_beer = num_of_beer
    num_of_beer -=1
    print (f' {curr_num_of_beer } bottles of beer on the wall. {curr_num_of_beer} bottle of beer. Take one down, pass it around, {num_of_beer} bottles of beer on the wall.')
    bottles_of_beer(num_of_beer)


def sum_of_decimal(num):
    '''
    :param num: the decimal number in which to add it individual digits
    :return sum: sum of the previous numbers
    '''
    if num < 10:
        return num

    digit = num % 10
    num = num - digit
    new_num = num / 10

    return sum_of_decimal(new_num) + digit