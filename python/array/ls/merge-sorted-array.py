from typing import List

class Solution:
    # TC: O(m + n) - We traverse through both arrays once.
    # SC: O(1) - We merge in-place, no extra space is used except for a few variables.
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays: nums1 and nums2. 
        The array nums1 has enough space (size m + n) to hold elements from both nums1 and nums2.
        Modifies nums1 in place to contain the merged result.

        :param nums1: List[int] - The first sorted array with space at the end to accommodate elements from nums2.
        :param m: int - The number of valid elements in nums1.
        :param nums2: List[int] - The second sorted array.
        :param n: int - The number of elements in nums2.
        :return: None - The result is stored in nums1.

        Idea:
        - Start from the end of both arrays, and merge them by placing the larger elements at the end of nums1.
        - This way, we don't overwrite elements in nums1 before we've compared them.

        Example:
            Input:
                nums1 = [1, 2, 3, 0, 0, 0], m = 3
                nums2 = [2, 5, 6], n = 3
            Process:
                Compare from the end of nums1 and nums2:
                - Compare 3 and 6 -> Place 6 at nums1[5]
                - Compare 3 and 5 -> Place 5 at nums1[4]
                - Compare 3 and 2 -> Place 3 at nums1[3]
                - Compare 2 and 2 -> Place 2 at nums1[2]
                - Compare 1 and 2 -> Place 2 at nums1[1]
                - Place remaining element 1 at nums1[0]
            Output: nums1 = [1, 2, 2, 3, 5, 6]
        """

        # Initialize two pointers for nums1 and nums2 starting from the last elements
        p1, p2 = m - 1, n - 1
        # Pointer for the last position in nums1
        p = m + n - 1
        
        # Merge the arrays by placing larger elements at the end of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If any elements are left in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
