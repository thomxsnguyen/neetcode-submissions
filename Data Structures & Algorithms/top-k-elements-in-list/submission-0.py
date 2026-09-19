class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for i, v in count.items():
            freq[v].append(i)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



