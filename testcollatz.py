

def test_collatz(n):
    verified_numbers = set()
    powers_of_two = {8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912}
    for i in range(5, n+1, 2):
        sequence = set()
        if i in powers_of_two:
            continue
        current = i
        while current >= i:
            if current in sequence:
                return False 
            sequence.add(current)

            if current % 2 == 1:
                if current in verified_numbers:
                    break 
                verified_numbers.add(current)
                current = 3*current + 1
            else:
                current /= 2




    return True  



def main():
    print(test_collatz(10000))


if __name__ == "__main__":
    main()  