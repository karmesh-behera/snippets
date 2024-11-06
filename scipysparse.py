import numpy, scipy.sparse


def main():
    n = 100000
    x = (numpy.random.rand(n) * 2).astype(int).astype(float) 
    x_csr = scipy.sparse.csr_matrix(x)
    x_dok = scipy.sparse.dok_matrix(x.reshape(x_csr.shape))

    print repr(x_csr)




if __name__ == "__main__":
    main()