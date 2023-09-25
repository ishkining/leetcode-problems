def dfs(node, adj, dp, vis):
    vis[node] = True

    for i in range(0, len(adj[node])):

        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis)

        dp[node] = max(dp[node], 1 + dp[adj[node][i]])


def addEdge(adj, u, v):
    adj[u].append(v)


def findLongestPath(adj, n):
    dp = [0] * (n + 1)

    vis = [False] * (n + 1)

    for i in range(1, n + 1):
        if not vis[i]:
            dfs(i, adj, dp, vis)

    ans = 0

    for i in range(1, n + 1):
        ans = max(ans, dp[i])

    return dp.index(ans)


n = int(input())
adj = [[] for i in range(n + 2)]
addEdge(adj, 0, 0)
for idx in range(1, n + 1):
    addEdge(adj, idx, int(input()))

print(findLongestPath(adj, n))
