
from typing import List

class Solution:
    # TC: O(n^2) - We iterate through each element of the matrix once.
    # SC: O(1) - The rotation is done in-place, so no extra space is used.
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the input n x n 2D matrix 90 degrees clockwise in-place.

        :param matrix: List[List[int]] - The input n x n matrix.
        :return: None - The matrix is modified in place (no need to return it).

        Idea:
        - First, transpose the matrix (swap rows and columns).
        - Then, reverse each row to achieve a 90-degree clockwise rotation.

        Example:
            Input: matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            Process:
                1. Transpose the matrix:
                   [
                       [1, 4, 7],
                       [2, 5, 8],
                       [3, 6, 9]
                   ]
                2. Reverse each row:
                   [
                       [7, 4, 1],
                       [8, 5, 2],
                       [9, 6, 3]
                   ]
            Output: matrix is rotated 90 degrees clockwise.
        """
        
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row to get the 90-degree rotation
        for i in range(n):
            matrix[i].reverse()
        
        # Example for matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        # Transpose step result:
        #   [
        #     [1, 4, 7],
        #     [2, 5, 8],
        #     [3, 6, 9]
        #   ]
        # Reverse rows step result:
        #   [
        #     [7, 4, 1],
        #     [8, 5, 2],
        #     [9, 6, 3]
        #   ]
