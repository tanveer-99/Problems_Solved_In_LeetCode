class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # to do it with the brute force approach, it would take O(n2)

        # for i in range(1, len(arr)):
        #     max = arr[i]
        #     for j in range(i+1, len(arr)):
        #         if arr[j] > max:
        #             max = arr[j]
        #     arr[i-1] = max
        # arr[-1] = -1
        # return arr

        # if we take the reverse iteration, then no extra memory would be needed
        # so it would be O(n)

        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            current_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = current_max
        return arr

