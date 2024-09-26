# leetcode Question 2
# https://leetcode.com/problems/valid-anagram/description/


# string = "aaii"
# string = "aiia"


class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return 1
