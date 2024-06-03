class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return False
        # return True

        for i in range(len(s) - 1):
            if s[i] < s[i+1]:
                

solution = Solution()

s = "racecar"

t = "carrace"

# should return true

print(solution.isAnagram(s, t))

s = "jar"

t = "jam"

# should return false

print(solution.isAnagram(s, t))
