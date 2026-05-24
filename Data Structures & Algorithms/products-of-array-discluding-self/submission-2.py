class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        z = 0

        for n in nums:
            if n == 0:
                z += 1
                continue
            p *= n

        res = []

        if z >= 2:
            return [0] * len(nums)

        if z == 1:
            res = [0] * len(nums)
            for i in range (0,len(res)):
                if nums[i] == 0:
                    res[i] = p
            return res

        if z == 0:
            for i in range(0, len(nums)):
                res.append(p//nums[i])
            return res