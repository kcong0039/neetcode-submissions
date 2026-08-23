from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []

        def helper(start: int, curr: List[int], total: int) -> None:
            if total == target:
                ret.append(curr.copy())
                return
            if total > target:
                return

            prev = None
            for i in range(start, len(candidates)):
                # skip duplicates at the same depth
                if candidates[i] == prev:
                    continue
                val = candidates[i]
                if total + val > target:
                    break  # further values only get larger
                curr.append(val)
                helper(i + 1, curr, total + val)  # use each number at most once
                curr.pop()
                prev = val

        helper(0, [], 0)
        return ret