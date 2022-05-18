class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        node_idx = 0
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        
        assignedid = [None] * n
        rank = [None] * n
        res = []

        def dfs(node, parent):
            nonlocal node_idx
            if rank[node] is not None:
                return

            assignedid[node] = rank[node] = node_idx  # Preorder Id Assignment "on the fly"
            node_idx += 1

            # 1. Preorder DFS on Undirected Graph
            for neigh in graph[node]:
                if neigh != parent:
                    dfs(neigh, node)
                    # Update Rank Postorder
                    if rank[neigh] < rank[node]:
                        rank[node] = rank[neigh]

            # 2. Critical connection
            # Neighbor Rank > Original Node means no cycle in between exists
            for neigh in graph[node]:
                if neigh != parent and rank[neigh] > assignedid[node]:
                    res.append([neigh, node])
                    

        dfs(0, None)

        return res