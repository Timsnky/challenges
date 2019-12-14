import math

def createSieve(number):
    startList = list(range(0, number + 1))

    startList[0] = False
    startList[1] = False

    print(startList)

def findNext(boolList, p):
    for key, value in enumerate(boolList):
        if key > p and value is True:
            return key

    return None

def list_true(n):
    values_list = []
    for number in range(0,n+1):
        if number == 0 or number == 1:
            values_list.append(False)
        else:
            values_list.append(number)
    return values_list

def find_next(bool_list, p):
    for key, value in enumerate(bool_list):
        if key > p and value is True:
            return key
    return None

def prime_from_list(bool_list):
    index_list = []
    for key, value in enumerate(bool_list):
        if value==True:
            index_list.append(key)
    return index_list

def is_prime_fast(number):
    if number == 2:
        return  True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        for factor in range(3, int(math.sqrt(number)) + 1, 2):
            if number % factor == 0:
                    return False
    return True

def get_primes(a, n):
    mylist=[]
    for number in range(a, n+1):
        if is_prime_fast(number):
            mylist.append(number)
    return mylist

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
        if p==3:
            return bool_list
    return prime_from_list(bool_list)

def mark_false(bool_list, p):
    for key, value in enumerate(bool_list):
        if key % p == 0 and key != p:
            bool_list[key] = False
        elif value is not True and value is not False:
            bool_list[key] = True
    return bool_list

test = sieve(20)
