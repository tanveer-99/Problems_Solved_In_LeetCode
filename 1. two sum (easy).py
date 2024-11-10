class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # if we use hashmaps, we can reduce the TC to O(n), with MC to O(n)
        hashmap = {}
        for index in range(0, len(nums)):
            difference = target - nums[index]
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[nums[index]] = index

        # to increase the difficulty, we could return how many times a match occurs

        # O(n*2) Time complexity solution:
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]