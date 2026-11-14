class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        pre = 1
        post = 1
        for num in nums[:-1]:
            pre = pre*num
            out.append(pre)
        # print(pre)
        # print(out)
        # print(out[-1])
        for i in range(len(nums)):
            out[-(i+1)] = post*out[-(i+1)]
            post = post * nums[-(i+1)]
        return out