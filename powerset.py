from math import log2 
def powerset(arr):
    n = len(arr)
    res = []
    for i in range(2**n):
        res.append(gen_subset(arr, i))
    return res


def gen_subset(arr, n):
    ls = [(i-1) for i, digit in enumerate(reversed(bin(n)), 1) if digit == '1']
    return [arr[i] for i in ls]

def genpowerset(s):
    power_set = []
    for int_for_subset in range(1 << len(s)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set


def main():

    '''arr = [3, 49, 29, 30, 39]
    print(gen_subset([3, 49, 29, 30, 39], 1))
    print(powerset(arr))
    print(len(powerset(arr)))'''
    arr = [3, 2, 4]
    print(powerset(arr))
    print(genpowerset(arr))
    

if __name__ == "__main__":
    main()