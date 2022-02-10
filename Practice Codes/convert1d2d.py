import numpy as np
def construct2DArray(original, m, n):
        arr = np.array(original)
        if (m == 1) and (n == 1):
            raise ValueError()
        arr2d = np.reshape(arr, (m,n))           
        return arr2d

original = [1,2]

construct2DArray(original,1,1)