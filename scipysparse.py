import numpy, scipy.sparse


def main():
    n = 10000
    #numpy.random.rand(n) - creates a numpy array with shape n and values drawn uniformly from (0, 1) where an array of shape n is an array of size n
    x = (numpy.random.rand(n) * 2).astype(int).astype(float) #x is an 1 x n numpy array with values chosen from the interval (0, 1), the type casts changes them to 0s and 1s
    x_csr = scipy.sparse.csr_matrix(x) # converts x to a compressed sparse row matrix
    x_dok = scipy.sparse.dok_matrix(x.reshape(x_csr.shape)) #dictionary of keys based sparse matrix, it takes a matrix x as argument, x is reshaped to x_csr's shape so that the two sparse matrices x_dok and x_csr have the same shape 


    #print(repr(x_csr))

# [0] * 2 = [0, 0]



if __name__ == "__main__":
    main()
