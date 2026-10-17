class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(arr)}
        visited = [False] * len(nums)
        swaps = 0
        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue
            cycle = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1
            swaps += cycle - 1
        return swaps