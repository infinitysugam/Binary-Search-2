# In this we perform 2 different binary search . One to find left index and second to find right index
# Time complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def searchRange(self, nums, target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]

        