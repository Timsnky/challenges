import math
# import time

def is_prime(number):
    if number == 2:
        return  True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        for factor in range(3, int(math.sqrt(number)) + 1, 2):
            if number % factor == 0:
                    return False
    return True

def is_mersenne_prime():
    myList = [2**number-1 for number in range(3, 65) if is_prime(number)]
    return myList

def ll_prime():
    mersenne_list = is_mersenne_prime()
    newlist = []
    for i in range(1,18):
        # print(i)
        # print(mersenne_list[i-1])
        # newlist.append((i, 1))
        if is_prime(mersenne_list[i-1]):
            newlist.append((i, 1))
        else:
            newlist.append((i, 0))
    return newlist
print(ll_prime())

# startTime = time.time()
# for num in range(1, 1000000000):
#     is_prime(num)
# end = time.time()
#
# print(end - startTime)