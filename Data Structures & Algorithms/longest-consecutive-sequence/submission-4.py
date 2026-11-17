class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq = []
        previous = -1e10
        length = 0
        long = 0
        for i in range(len(nums)):
            if seq == []:
                seq.append(nums[i])
                length += 1
                if long < length:
                    long = length
            elif nums[i] - seq[-1] == 1:
                seq.append(nums[i])
                length += 1
                if long < length:
                    long = length
                    # print(seq)
            elif nums[i] - seq[-1] == 0:
                continue
            else:
                seq = []
                seq.append(nums[i])
                length = 0
                length += 1
        return long