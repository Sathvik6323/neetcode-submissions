class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col=set()
        posdiag=set() #r+c
        negdiag=set() #r-c
        board =[["."]*n for i in range(n)]
        res=[]

        def backtracking(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or r-c in negdiag or r+c in posdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"

                backtracking(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."

        
        backtracking(0)
        return res

        