MASK_SIZE = 16
BIT_MASK = 0xFFFF

def divide(x, y):
    if y > x:
        return 0
    k = 0
    while (y << (k+1)) < x:
        k += 1
    remainder, count = x - (y << k), 0

    while remainder > y:
        remainder -= y
        count += 1


    return (1 << k) + count 


def main():
    print(divide(43, 6))

if __name__ == "__main__":
    main()