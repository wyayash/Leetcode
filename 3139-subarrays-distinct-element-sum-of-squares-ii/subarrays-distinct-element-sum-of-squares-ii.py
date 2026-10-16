class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def push_down(node, start, end):
            if lazy[node] == 0:
                return
            
            mid = (start + end) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            val = lazy[node]
            
            len_left = mid - start + 1
            sum2[left_node] = (sum2[left_node] + 2 * val * sum1[left_node] + len_left * val * val) % MOD
            sum1[left_node] = (sum1[left_node] + len_left * val) % MOD
            lazy[left_node] = (lazy[left_node] + val) % MOD
            len_right = end - mid
            sum2[right_node] = (sum2[right_node] + 2 * val * sum1[right_node] + len_right * val * val) % MOD
            sum1[right_node] = (sum1[right_node] + len_right * val) % MOD
            lazy[right_node] = (lazy[right_node] + val) % MOD
            lazy[node] = 0
        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                length = end - start + 1
                sum2[node] = (sum2[node] + 2 * val * sum1[node] + length * val * val) % MOD
                sum1[node] = (sum1[node] + length * val) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            push_down(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD
        total_sum = 0
        last_pos = {}
        for j, num in enumerate(nums):
            prev_idx = last_pos.get(num, -1)
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            total_sum = (total_sum + sum2[1]) % MOD
            last_pos[num] = j
        return total_sum