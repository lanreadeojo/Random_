def fizzbuzz():
    fizz = "fizz"
    buzz = "buzz"
    fizz_buzz = "fizzbuzz"
    x = 0
    while x <100:
        x = x+1
        if x % 15 == 0:
            print(f' {fizz_buzz} {x}')
        elif x % 3 == 0:
            print(f' {fizz} {x}')
        elif x % 5 == 0:
            print(f' {buzz} {x}')
        else:
            print (x)


fizzbuzz()
