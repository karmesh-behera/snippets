
def parity(x):
    result = 0 
    while x:
        result ^= 1
        x &= x - 1
    return result 


def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result



def main():
    x = parity(102020)
    print(parity(x))

if __name__ == "__main__":
    main()