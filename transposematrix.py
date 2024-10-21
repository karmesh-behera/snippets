import numpy as np

def main():
    a = [(1,2,3),(4,5,6)]
    x = list(zip(*a))
    b = [(1,2),(3,4),(5,6)]
    y = list(zip(*b))
    for i in x:
        print(i)
    
    a = np.array([[1, 2], [3, 4]])
    for i in a:
        print(a)
    
    a.transpose()
    for i in a:
        print(a)






if __name__ == "__main__":
    main()