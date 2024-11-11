class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
      class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        r=len(grid)
        c=len(grid[0])
        seen=set()
        ans=0
        def help(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]=='W' or (i,j) in seen:
                return
            seen.add((i,j))
            help(i+1,j)
            help(i,j+1)
            help(i-1,j)
            help(i,j-1)
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and grid[i][j]=='L':
                    help(i,j)
                    ans+=1
                    
        return ans
                    
        return 0
