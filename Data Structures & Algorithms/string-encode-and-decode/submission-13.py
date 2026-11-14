class Solution:

    def encode(self, strs: List[str]) -> str:
        # Appends the delimiter to every single string, even empty ones
        return "".join(s + chr(257) for s in strs)
    def decode(self, s: str) -> List[str]:
        # Split will naturally produce an extra empty string at the end.
        # slicing [:-1] removes it.
        return s.split(chr(257))[:-1]
