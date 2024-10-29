def permutation(perm, arr):
    for i in range(len(arr)):
        next = i
        while perm[next] >= 0:
            arr[i], arr[perm[next]] = arr[perm[next]], arr[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]
    
# THE ESSENTIAL IDEA IS we break the permutation down into cycles, and when we apply a cycle, we subtract n so the value stays the same, only with a signed bit 
# this way we know that we've already applied a permutation and can skip it 
#
def main():
    arr = ['a', 'b', 'c', 'd']
    print(arr)
    perm = [2,0,1,3]
    # expected output [b,c,a,d]
    permutation(perm, arr)
    print(arr)


if __name__ == "__main__":
    main()