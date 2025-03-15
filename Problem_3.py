# For this we check if mid is greater than neighbour then return the mid.
# Else we go the the half array which has greater neighbour then mid
# Time Complexity = O(logn)
# Space Complexity = O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = low + (high-low)//2

            if (mid==0 or nums[mid]>nums[mid-1]) and (mid ==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            
            elif mid == len(nums)-1 or nums[mid+1] > nums[mid]:
                low = mid + 1
            else:
                high = mid -1

            
        