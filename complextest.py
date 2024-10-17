from Complex.py import Complex


def main():
    z = Complex(2, 3)
    w = Complex(4, 5)
    y = z.div(w)


    print(str(z))
    print(str(w))
    print(str(y))


if __name__ == "__main__":
    main()