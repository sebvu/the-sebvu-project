class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # big difference, in this solution it uses a hashmap. i do not use a hashmap, and instead use match case.

        for c in s:  # iterate through s
            if c in closeToOpen:  # check if c is a closing bracket
                if (
                    stack and stack[-1] == closeToOpen[c]
                ):  # verify if it matches with current stack
                    stack.pop()  # remove due to LIFO
                else:
                    return False  # if conditions do not match, return False
            else:
                stack.append(c)  # append any opening to stack

        return (
            True if not stack else False
        )  # i didn't even know you could do conditions like this


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
