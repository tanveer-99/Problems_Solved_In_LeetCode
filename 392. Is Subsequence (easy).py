class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
                continue
            continue
        if i == len(s):
            return True
        else:
            return False

# the time complexity of this solution is O(n)

# An observation:
    # this solution takes 0 ms runtime, and if i solve this with a while loop, it takes 28 ms runtime. why?
    # because of python's internal optimization, a for loop has fixed ranges and boundaries and a while loop wil iterate
    # every time until it gets an edge case, so it will check for conditions every time
    # so, the overhead becomes relatively greater for while loops than for loops.
    # so, the extra runtime generates from being checking the conditions is every loop, while a for loop just knows that
    # i have to execute for this certain period.