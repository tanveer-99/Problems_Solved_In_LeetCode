class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # this solution may contain some space but saves time complexity
        # by using hashset, TC: O(n) SC: O(n)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

# sorting the array and matching the adjacent numbers: TC: O(nlogn), SC: O(1)

        # n = len(nums)
        # sort_nums = sorted(nums)
        # for i in range(n-1):
        #     if sort_nums[i] == sort_nums[i+1]:
        #         return True
        #         break
        # return False


# the brute force solution: TC: O(n*2), SC: O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True

        # return False