class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        missingNums = []

        for i, n in enumerate(range(1, len(nums))):
            if nums[i] != n:
                missingNums.append(n)

        return missingNums

nums = [4, 6, 1, 6, 7, 4, 1]
print(Solution().findDisappearedNumbers(nums))
# [2, 3, 5]
