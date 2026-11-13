class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        majority = (0, 0)

        for f in freq:
            if freq[f] > majority[1]:
                majority = (f, freq[f])

        return majority[0]
        