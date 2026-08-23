class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(matrix, lo, hi, target):
            if hi-lo==1:
                return lo
            else:
                mid = (hi+lo)//2
                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    return mid
                elif target > matrix[mid][-1]:
                    return bs(matrix, mid, hi, target)
                else:
                    return bs(matrix, lo, mid, target)
        row = bs(matrix, 0, len(matrix), target)
        return target in matrix[row]

