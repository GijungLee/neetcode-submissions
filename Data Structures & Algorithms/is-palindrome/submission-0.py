class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[^a-zA-Z0-9]"
        result = re.sub(regex, "", s).lower()
        print(result)
        for i in range(len(result)//2):
            if result[i] != result[-(i+1)]:
                return False
        return True