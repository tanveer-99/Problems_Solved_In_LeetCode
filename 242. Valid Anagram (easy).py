class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # we can do this by sorting the strings first and then matching
        # assuming the sorting function takes O(1), different sort functions take different.
        # a sort function of my own would also help.
        return sorted(s) == sorted(t)

        # we can do this with python counter functions with just one line

        return Counter(s) == Counter(t)

        # we can do this with hashmaps, storing the characters on hashmaps and
        # then matching the hashmaps characters
        # TC: O(s+t), SC:O(s+t)

        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True