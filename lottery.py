import random


def lottery():
    no_match = "$0"
    one_match = "$1,000.00"
    two_match = "$10,000.00"
    match = "$100,000.00"
    num1 = str(random.randint(0,9))
    num2 = str(random.randint(0,9))
    the_num = num1 + num2
    print('The number was: {}'.format(the_num))
    resp = input("Please guess your first number - (0-9): ")
    resp2 = input("Please guess your first number - (0-9): ")
    the_resp = resp + resp2
    print('You guessed {}'.format(the_resp))
    print('The number was: {}'.format(the_num))
    if(the_resp == the_num):
        return 'You win: {}'.format(match)
    if (the_resp != the_num):
        if (resp == num1 or resp == num2):
            return 'You win: {}'.format(one_match)
        if (resp2 == num1 or resp2 == num2):
            return 'You win: {}'.format(one_match)
    if (the_resp != the_num):
        return 'You win: {}'.format(no_match)



print(lottery())