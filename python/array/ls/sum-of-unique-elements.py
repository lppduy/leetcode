from typing import List

class Solution:
    # TC: O(n) - We traverse the array once to count elements and once to sum the unique elements.
    # SC: O(n) - We use extra space to store the count of elements.

    def sumOfUnique(self, nums: List[int]) -> int:
        """
        Returns the sum of all unique elements in the array nums.

        :param nums: List[int] - The input array of integers.
        :return: int - The sum of all unique elements in the array.

        Idea:
        - First, we use a dictionary to count the occurrences of each element in nums.
        - Then, we sum the elements that appear exactly once.

        Example:
            Input: nums = [1, 2, 3, 2]
            Process:
                Count frequencies: {1: 1, 2: 2, 3: 1}
                Sum unique elements: 1 + 3 = 4
            Output: 4
        """

        # Step 1: Count the occurrences of each element
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Sum only the elements that appear exactly once
        unique_sum = 0
        for num, freq in count.items():
            if freq == 1:
                unique_sum += num
        
        return unique_sum
