class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        # print(newStr)
        # print(newStr[::-1])
        return newStr == newStr[::-1]