class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = rows * cols - 1 

        while left <= right:
            midindex = (left + right)  // 2
            row = midindex // cols
            col = midindex % cols

            mid_value = matrix[row][col]

            if mid_value == target:
                return True

            if mid_value < target:
                left = midindex + 1

            if mid_value > target:
                right = midindex - 1

        return False 
        
