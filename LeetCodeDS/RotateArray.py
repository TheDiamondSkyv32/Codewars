"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 10**5
-2**31 <= nums[i] <= 2**31 - 1
0 <= k <= 10**5
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # make sure k is smaller than length of nums, we don't want to go out of bounds 
        # arr[1,2,3,4] --> we don't want to access arr[4] by accident

        l, r = 0, len(nums) - 1 # left & right pointers pointing at the start and end of array
        while l < r: # reverse the array --> when l and r touch, the array has been reversed
            nums[l], nums[r] = nums[r], nums[l] 
            l, r = l + 1, r - 1

        l, r = 0, k - 1 # reverse the first K elements 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] 
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1 # reverse the K to end of array elements 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] 
            l, r = l + 1, r - 1
