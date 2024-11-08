import numpy as np
from scipy import ndimage 


def calculate_target_size(img_size: int, filter_size: int) -> int:
    num_pixels = 0
    for i in range(img_size):
        added = i + filter_size
        if added <= img_size:
            num_pixels += 1
            
    return num_pixels

def convolve(img: np.array, filter: np.array) -> np.array:
    tgt_size = calculate_target_size(img_size=img.shape[0], filter_size=filter.shape[0])
    k = filter.shape[0]
    
    convolved_img = np.zeros(shape=(tgt_size, tgt_size))
    
    for i in range(tgt_size):
        for j in range(tgt_size):
            mat = img[i:i+k, j:j+k]
  
            convolved_img[i, j] = np.sum(np.multiply(mat, filter))
            
    return convolved_img

def main():
    rng = np.random.default_rng(123)
    arr = rng.normal(size=(5,5,3)).round(2)
    filter = rng.normal(size=(5,5,3)).round(2)

    arr2 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    filter2 = np.array([[1,-1],[0,1]])

    #print(convolve(arr, filter))

    print(convolve(arr2, filter2))
    print(ndimage.convolve(arr2, filter2))
    #print(ndimage.correlate(arr2, filter))
    #print(np.convolve([1, 1, 1], [1, 1]))


if __name__ == "__main__":
    main()