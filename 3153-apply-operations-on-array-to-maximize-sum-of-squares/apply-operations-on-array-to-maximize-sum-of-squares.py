from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        bit_counts = [
            sum((x >> i) & 1 for x in nums)
            for i in range(30)
        ]

        result = 0

        for _ in range(k):
            current_num = 0

            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= 1 << i
                    bit_counts[i] -= 1

            result = (result + current_num * current_num) % MOD

        return result