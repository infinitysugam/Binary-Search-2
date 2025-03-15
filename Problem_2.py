# TO find the minimum we first if array is already sorted then return arr[0]
# Else we check if mid is minimum by checking its neighbour
# Else we go into the unsorted array and repeat the same steps
# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def findMin(self, nums) -> int:
        low = 0 
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[low]<=nums[high]:
                return nums[low]
            
            if nums[mid] < nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            
            if nums[mid] >= nums[low]:
                low = mid+1
            else:
                high = mid -1 
            
