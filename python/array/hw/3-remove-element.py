from typing import List

class Solution:
    # TC: O(n) - We traverse the array once, so the time complexity is linear.
    # SC: O(1) - No additional space is used aside from a few variables, so the space complexity is constant.

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in-place and return the new length.
        
        The order of the elements may be changed. It doesn't matter what values are set beyond the new length.

        :param nums: List[int] - The input array of integers.
        :param val: int - The value to be removed from the array.
        :return: int - The new length of the array after removing all instances of val.

        Idea:
        Use two pointers:
        - Pointer `i` iterates over each element of the array.
        - Pointer `k` keeps track of the position where elements that are not equal to `val` should be placed.
        Whenever `nums[i]` is not equal to `val`, it gets placed at `nums[k]`, and `k` is incremented.

        This approach ensures that all occurrences of `val` are removed, and the remaining elements are placed at the beginning of the array.

        Example:
            Input: nums = [3, 2, 2, 3], val = 3
            Process:
                - nums[0] = 3, skip it.
                - nums[1] = 2, move it to nums[0].
                - nums[2] = 2, move it to nums[1].
                - nums[3] = 3, skip it.
            Result: New length = 2, array = [2, 2]
        """
        
        # Pointer `k` to track the position for placing elements not equal to `val`
        k = 0
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # If the current element is not equal to `val`, place it at position `k` and increment `k`
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # Return the new length (all elements before index `k` are valid)
        return k
