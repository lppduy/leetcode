from typing import List

class NumArray:
    # TC: O(1) for each sumRange call - The sum is precomputed, so each query is handled in constant time.
    # SC: O(n) - We store the prefix sum of the array.

    def __init__(self, nums: List[int]):
        """
        Initializes the NumArray object with the integer array nums.

        :param nums: List[int] - The input array of integers.
        
        Idea:
        - We use a prefix sum array to store cumulative sums. This allows us to compute the sum of any subarray 
          in constant time by subtracting the appropriate values from the prefix sum.
        - prefix_sum[i] will store the sum of elements from nums[0] to nums[i-1]. 
        """
        # Initialize the prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)

        # Compute the prefix sums
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + ... + nums[right]).

        :param left: int - The left index of the range.
        :param right: int - The right index of the range.
        :return: int - The sum of elements between indices left and right.

        Example:
            Input: nums = [-2, 0, 3, -5, 2, -1], sumRange(0, 2)
            Process:
                prefix_sum = [0, -2, -2, 1, -4, -2, -3]
                To get sumRange(0, 2): 
                Use prefix_sum[3] - prefix_sum[0] = 1 - 0 = 1
            Output: 1
        """
        # The sum of range [left, right] is calculated by:
        # prefix_sum[right + 1] - prefix_sum[left]
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
