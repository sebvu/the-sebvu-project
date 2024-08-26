class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        indexStack = []
        openingPair = ""

        for i in range(len(s)):
            match s[i]:
                case ")":
                    openingPair = "("
                case "}":
                    openingPair = "{"
                case "]":
                    openingPair = "["
                case _:  # for all opening pairs
                    indexStack.append(i)
                    continue

            if len(indexStack) == 0 or s[indexStack[-1]] != openingPair:
                return False
            else:
                indexStack.pop()

        if len(indexStack) == 0:
            return True
        else:
            return False


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
