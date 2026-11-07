class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        for i, num in enumerate(nums_sorted):
            freq[num].append(1)
        freq2 = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        # print(freq2)
        topk = []
        for i, (key, value) in enumerate(freq2.items()):
            if i < k:
                topk.append(key) 
            else:
                pass
        # while len(topk) < k:
                # topk.append(freq2.items().pop()[0])
        return topk