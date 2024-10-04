from typing import List

class Solution:
    # TC: O(n^2) - We are generating numRows rows, and each row i has i elements.
    # SC: O(n^2) - We are storing the entire triangle in memory.
    
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate the first numRows of Pascal's Triangle.
        :param numRows: int - The number of rows to generate
        :return: List[List[int]] - Pascal's Triangle represented as a list of lists

        Idea: Each row starts and ends with 1. 
        The internal elements are the sum of two elements directly above it from the previous row.

        For example:
            For row 4 (i = 4), we calculate internal elements:
                row[1] = triangle[3][0] + triangle[3][1] = 1 + 3 = 4
                row[2] = triangle[3][1] + triangle[3][2] = 3 + 3 = 6
                row[3] = triangle[3][2] + triangle[3][3] = 3 + 1 = 4
            So row 4 will be: [1, 4, 6, 4, 1]
        """
        triangle = [] 
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle  
