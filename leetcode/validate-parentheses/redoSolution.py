class Solution:
    def isValid(self, s: str) -> bool:
        # more efficient:
        # - better memory usage (no openingPair variable, no storing the indices (which takes up more memory then the strings themselves)
        # - the dictionary memory never changes because it is constant, with stack being the only memory takeup

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:  # iterate through all characters
            if c in closeToOpen:  # will be true if c is a key in closeToOpen
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return (
            True if not stack else False
        )  # will return True if stack is EMPTY, else False


solution = Solution()

string1 = "[]"  # true
string2 = "([{}])"  # true
string3 = "[(])"  # false
string4 = "()[]{}"  # true
string5 = "]]"  # false
string6 = "(("  # false

print(solution.isValid(string1))
print(solution.isValid(string2))
print(solution.isValid(string3))
print(solution.isValid(string4))
print(solution.isValid(string5))
print(solution.isValid(string6))
