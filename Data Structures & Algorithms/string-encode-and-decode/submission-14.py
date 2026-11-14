class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(258) # Special character strictly for empty lists
        return chr(257).join(strs)
    def decode(self, s: str) -> List[str]:
        if s == chr(258):
            return []
        return s.split(chr(257))