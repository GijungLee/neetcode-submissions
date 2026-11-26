class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        # Try each unique character as the one we want to keep
        for target in set(s):
            l = 0
            used = 0

            for r in range(len(s)):
                if s[r] != target:
                    used += 1

                # Shrink window until replacements used <= k
                while used > k:
                    if s[l] != target:
                        used -= 1
                    l += 1

                longest = max(longest, r - l + 1)

        return longest