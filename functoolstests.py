from functools import reduce 
def parity(n):
    if n % 2 == 1:
        return True
    else:
        return False
def main():
    print(reduce(lambda x, y: x+y, [1,2,3,4,5]))
    print(reduce(lambda x, y: x*y + y^2, [1,2,3,4,5]))
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    sequence = [23, 30, 1, 2, 4, 5, 9, 3]
    odd = filter(lambda p : p % 2 != 0, sequence)

    for s in odd:
        print(s, end=' ')

    #filtered = filter(parity, sequence)
    #for s in filtered:
    #    print(s)
    




if __name__ == "__main__":
    main()