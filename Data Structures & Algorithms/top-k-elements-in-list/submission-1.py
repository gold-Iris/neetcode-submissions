class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1

        sorted_count = dict(
            sorted(count.items(), key=lambda item: item[1], reverse=True)
        )

        keys = list(sorted_count.keys())
        return keys[:k]