class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi = nums[0]
        currsum = 0

        for i in nums:
            if currsum < 0:
                currsum = 0
            currsum += i

            maxi = max(maxi, currsum)
        return maxi

