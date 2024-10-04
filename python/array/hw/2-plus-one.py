from typing import List

class Solution:
    # TC: O(n) - We iterate over the list of digits once, so the time complexity is linear.
    # SC: O(1) - We only modify the input list in place and do not use extra space (except for the result if necessary).

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Add one to the number represented by the list of digits.
        
        :param digits: List[int] - The list of digits representing a large non-negative integer.
        :return: List[int] - The list of digits representing the number after adding one.

        Idea: 
        Start from the last digit (least significant) and try to add one. If the digit is less than 9, we can simply add one 
        and return the result. If the digit is 9, we set it to 0 and continue to the next digit. If all digits are 9, we append 
        a 1 at the front of the list to handle the carry.

        Example:
            Input: [1, 2, 9]
            Process:
                Start at the last digit: 9 -> Set to 0 and carry 1.
                Move to the next digit: 2 -> Add 1 -> 3.
            Result: [1, 3, 0]

            Input: [9, 9, 9]
            Process:
                Start at the last digit: 9 -> Set to 0 and carry 1.
                Repeat for all digits.
                After processing all, append 1 at the front.
            Result: [1, 0, 0, 0]
        """
        
        # Iterate from the last digit to the first one (right to left)
        for i in reversed(range(len(digits))):
            # If current digit is less than 9, just add one and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, set it to 0 (carry over)
            digits[i] = 0
        
        # If all digits are 9 (e.g. [9, 9, 9]), we need to add 1 at the beginning
        return [1] + digits
