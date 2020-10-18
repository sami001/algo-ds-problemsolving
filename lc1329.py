#matrix

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat[0])):
            temp = []
            for j in range(len(mat)):
                if i+j < len(mat[0]):
                    temp.append(mat[j][j+i])
            temp.sort()
            for j in range(len(temp)):
                    mat[j][j+i] = temp[j]
        
        for i in range(1, len(mat)):
            temp = []
            for j in range(len(mat[0])):
                if i+j < len(mat):
                    temp.append(mat[i+j][j])
            temp.sort()
            for j in range(len(temp)):
                if i+j < len(mat):
                    mat[i+j][j] = temp[j]
        return mat
            
                
            
        
