import numpy as np

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        matrix = np.array(matrix)
        matrix = np.ravel(matrix)
        matrix = np.sort(matrix)
        
        return matrix[k-1]