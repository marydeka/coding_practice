
'''
Problem: Matrix Search
Iteration: 1
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0 or n == 0:
            return False
        
        combined_arr = []
        
        #combine all arrays into single array to perform binary search
        for arr in matrix:
            combined_arr += arr
            
        #perform binary search
        start = 0
        end = len(combined_arr) - 1
        
        print(combined_arr)
        
        while start <= end:
            # print(f"start: {start}")
            # print(f"end: {end}")
        
            mid = start + (end - start) // 2
            # print(f"mid: {mid}")
            # print(combined_arr[mid])
            if target == combined_arr[mid]:
                return True
            elif target < combined_arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False