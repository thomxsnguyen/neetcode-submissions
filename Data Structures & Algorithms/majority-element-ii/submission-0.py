class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        output = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        
        for key, value in freq.items():
            if value > (n/3):
                output.append(key)
        return output