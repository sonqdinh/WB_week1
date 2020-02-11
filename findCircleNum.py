class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
#         # Union _ Disjoint set:
#         friend_circle = N = len(M)
        
#         friends = list(range(N))
        
#         def find(a):
#             while friends[a] != a:
#                 a = friends[a]
#             return a
        
#         def union(a,b):
#             friends[a] = b
            
#         for r in range(N):
#             for c in range(r + 1, N):
#                 if M[r][c] == 1:
#                     r_lead, c_lead = find(r), find(c)
#                     if r_lead != c_lead:
#                         union(r_lead, c_lead)
#                         friend_circle -= 1
        
#         return friend_circle
        # DFS:
        N = len(M)
        visited = [False] * N
        
        def dfs(n):
            for i in range(N):
                if M[n][i] and not visited[i]:
                    visited[i] = True
                    dfs(i)
        
        total_circle = 0
        for i in range(N):
            if not visited[i]:
                total_circle += 1
                visited[i] = True
                dfs(i)
        
        return total_circle
            
        
        