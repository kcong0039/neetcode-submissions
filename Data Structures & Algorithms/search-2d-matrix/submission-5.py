class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.bsR(matrix, 0, len(matrix), target)
        if row == -1:
            return False
        return target in matrix[row]
    def bsR(self, matrix, lo, hi, target):
        mid = (hi+lo)//2
        if hi-lo == 1:
            if matrix[lo][0] <= target <= matrix[lo][-1]:
                return lo
            return -1
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        elif matrix[mid][0] >= target:
            return self.bsR(matrix, lo, mid, target)
        else:
            return self.bsR(matrix, mid, hi, target)

