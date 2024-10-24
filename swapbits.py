MASK_SIZE = 16
BIT_MASK = 0xFFFF

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def main():
    print()

if __name__ == "__main__":
    main()