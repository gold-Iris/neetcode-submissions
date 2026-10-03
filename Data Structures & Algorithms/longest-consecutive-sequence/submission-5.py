class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=0
        s_nums=set(nums)
        for x in s_nums:
            counter=0
            if x-1 not in s_nums:
                a=x
                while a in s_nums:
                    counter+=1
                    a+=1
                result=max(result,counter)

        return result