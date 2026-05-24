class Solution:

    def binsearch(self, arr: List[int], target: int) -> bool:
        n = len(arr)

        low, high = 0, n-1

        while(low <= high):
            mid = (low + ((high -low)//2))

            if (arr[mid] == target):
                return True
            
            if (arr[mid] > target):
                high = mid-1
            else:
                low = mid+1
        return False




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        res = False

        for r in range (0, m):
            if (matrix[r][0] == target or matrix[r][n-1] == target):
                return True


            if matrix[r][n-1] < target:
                continue

            elif (matrix[r][0] <= target < matrix[r][n-1]):
                res = self.binsearch(matrix[r], target)
        return res

        '''for r in range(0, m):
            for c in range(0, n):
                
                if (matrix[r][n-1] < target):
                    continue

                elif (matrix[r][0] <= target < matrix[r][n-1]):
                    for n in range(0, n):
                        if (target == matrix[r][n]):
                            res = True

        return res'''