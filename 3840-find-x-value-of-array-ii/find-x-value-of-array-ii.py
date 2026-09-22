class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        tree = [(1 % k, [0] * k) for _ in range(2 * size)]
        def merge(left, right):
            lp, lc = left
            rp, rc = right
            cnt = lc[:]
            for r in range(k):
                cnt[(lp * r) % k] += rc[r]

            return (lp * rp) % k, cnt

        for i, num in enumerate(nums):
            r = num % k
            cnt = [0] * k
            cnt[r] = 1
            tree[size + i] = (r, cnt)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        def update(index, value):
            pos = size + index
            r = value % k
            cnt = [0] * k
            cnt[r] = 1
            tree[pos] = (r, cnt)
            pos //= 2
            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(l, r):
            left_res = (1 % k, [0] * k)
            right_res = (1 % k, [0] * k)
            l += size
            r += size
            while l < r:
                if l % 2:
                    left_res = merge(left_res, tree[l])
                    l += 1
                if r % 2:
                    r -= 1
                    right_res = merge(tree[r], right_res)
                l //= 2
                r //= 2
            return merge(left_res, right_res)
        ans = []
        for index, value, start, x in queries:
            update(index, value)
            _, cnt = query(start, n)
            ans.append(cnt[x])
        return ans