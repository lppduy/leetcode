from typing import List

class Solution:
    # TC: O(n) - We traverse the array twice, once for the left products and once for the right products.
    # SC: O(1) - The space complexity is constant if we don't count the result array as extra space, 
    # otherwise it's O(n) due to the result array.

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements 
        of nums except nums[i].

        You must solve it without using division and in O(n) time.

        :param nums: List[int] - The input array of integers.
        :return: List[int] - The array where each element is the product of all other elements except itself.

        Idea:
        - First pass: Compute the products of all elements to the left of each index.
        - Second pass: Compute the products of all elements to the right of each index and multiply them with the 
          left products stored in the result array.
        
        We achieve the result without using extra arrays for left and right products, 
        instead we update the result array in-place.

        Example:
            Input: nums = [1, 2, 3, 4]
            Process:
                Left pass: result = [1, 1, 2, 6] (storing products of elements to the left)
                Right pass and final result: result = [24, 12, 8, 6] (multiply right products with result)
        """

        # Initialize the result array with 1s, which will hold the left products initially
        n = len(nums)
        result = [1] * n
        
        # First pass: Calculate left products for each element
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]  # Update left product for the next element
        
        # Example of first pass for nums = [1, 2, 3, 4]:
        # After index 0: result = [1, 1, 1, 1] (left_product = 1)
        # After index 1: result = [1, 1, 1, 1] (left_product = 2)
        # After index 2: result = [1, 1, 2, 1] (left_product = 6)
        # After index 3: result = [1, 1, 2, 6] (left_product = 24)
        
        # Second pass: Calculate right products and multiply with the left products in the result array
        right_product = 1
        for i in reversed(range(n)):
            result[i] *= right_product  # Multiply with the right product
            right_product *= nums[i]  # Update right product for the next element
        
        # Example of second pass for nums = [1, 2, 3, 4]:
        # After index 3: result = [1, 1, 2, 6] (right_product = 4)
        # After index 2: result = [1, 1, 8, 6] (right_product = 12)
        # After index 1: result = [1, 12, 8, 6] (right_product = 24)
        # After index 0: result = [24, 12, 8, 6] (right_product = 24)
        
        return result
