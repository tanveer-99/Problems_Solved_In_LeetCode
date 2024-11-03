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
