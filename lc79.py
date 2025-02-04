#backtracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        r = len(board)
        c = len(board[0])
        vis = [[False for j in range(c)] for i in range(r)]

       

        def back(i, j, ln):
            if ln == len(word)-1:
                return True

            vis[i][j] = True
            ret = False
            for (ii, jj) in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if ii >= 0 and ii < r and jj >= 0 and jj < c and board[ii][jj] == word[ln+1] and vis[ii][jj] == False:             
                    ret |= back(ii, jj, ln+1)
            vis[i][j] = False
            return ret

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if(back(i, j, 0) == True):
                        return True
        return False

        
