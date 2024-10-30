
import heapq
from itertools import islice
from math import sqrt 
import numpy as np 
import random
import time

def randomTriplet(n):
    num = 0
    while True:
        yield (random.randrange(n), random.randrange(n), random.randrange(n))
        num += 1


def iterstars(k, stream):
    max_heap = [(-1*(sqrt(s[0]**2 + s[1]**2 + s[2]**2)), s) for s in islice(stream, k)]
    heapq.heapify(max_heap)
    x = randomTriplet(10**5)
    for i in range(10**5):
        s = next(x)
        heapq.heappushpop(max_heap, (-1*(sqrt(s[0]**2 + s[1]**2 + s[2]**2)), s))
    return [q[1] for q in max_heap]


def stars(k, stream):
    max_heap = [(-1*(sqrt(s[0]**2 + s[1]**2 + s[2]**2)), s) for s in islice(stream, k)]
    heapq.heapify(max_heap)
    stream = []

    for i in range(10**5):
        temp = [random.randrange(10**5), random.randrange(10**6), random.randrange(10**5)]
        stream.append(temp)    
    for s in stream:
        heapq.heappushpop(max_heap, (-1*(sqrt(s[0]**2 + s[1]**2 + s[2]**2)), s))
    return [q[1] for q in max_heap]





def main():
    stream = []
    '''
    for i in range(10**5):
        temp = [random.randrange(10**5), random.randrange(10**6), random.randrange(10**5)]
        stream.append(temp)
    
    t0 = time.time()
    x = stars(8, stream)
    t1 = time.time()
    print(x)
    stream = []'''

    for i in range(10):
        temp = [random.randrange(10**5), random.randrange(10**5), random.randrange(10**5)]
        stream.append(temp)
    t2 = time.time()
    x = iterstars(8, stream)
    t3 = time.time()
    print(x)
    print('time taken without the generator optimization is ' + str(t1-t0) + ' seconds and the time taken with the optimization is ' + str(t3-t2) + ' seconds.')



if __name__ == "__main__":
    main()