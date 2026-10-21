class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        def ok(k: int) -> bool:
            prev_max = 0  
            for start in range(0, n, k):
                block = nums[start:start + k]
                desc = 0
                for i in range(k - 1):
                    if block[i] > block[i + 1]:
                        desc += 1
                        if desc > 1:
                            return False
                if block[-1] > block[0]:
                    desc += 1
                    if desc > 1:
                        return False
                if min(block) < prev_max:
                    return False
                prev_max = max(block)
            return True
        for k in range(1, n + 1):
            if n % k == 0 and ok(k):
                total += k
        return total