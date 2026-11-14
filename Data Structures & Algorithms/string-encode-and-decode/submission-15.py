class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(258)
        encoded_string = chr(257).join(strs)
        # print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == chr(258):
            return []
        decoded_strs = s.split(chr(257))
        # print(decoded_strs)
        return decoded_strs


