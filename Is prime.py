def is_prime(x):
    if x <= 1:
        print('Isnt prime')
        return False
    elif x == 2:
        print('Is prime')
        return True
    elif x > 1:
        for n in range(2,x):
            if x % n == 0:
                print('Isnt prime')
                return False
    return True
