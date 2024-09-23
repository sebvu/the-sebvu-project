class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):
            for c in s:
                matchingCharacterIndex = t.find(c)
                if matchingCharacterIndex != -1:
                    
                else:
                    return False
        else:
            return False
        return True


solution = Solution()

s = "racecar"

t = "carrace"

# should return true

print(solution.isAnagram(s, t))

s = "jar"

t = "jam"

# should return false

print(solution.isAnagram(s, t))
