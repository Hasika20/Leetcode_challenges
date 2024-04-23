class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]
        ed = {i: set() for i in range(n)}
        for [n1, n2] in edges:
            ed[n1].add(n2)
            ed[n2].add(n1)

        running = set(range(n))
        c = [i for i in range(n) if len(ed[i]) < 2 ]
        while len(running) > 2:
            nb = set()
            for i in c:

                running.remove(i)
                for j in ed[i]:
                    ed[j].remove(i)
                    if len(ed[j]) < 2:
                        nb.add(j)
            c = nb
        return list(sorted(running))