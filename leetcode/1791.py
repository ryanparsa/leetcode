from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # time: O 1
        # space O 1
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]

    def findCenter(self, edges: List[List[int]]) -> int:
        # time: O n
        # space O n

        counter = dict()
        for edge in edges:
            counter[edge[0]] = counter.get(edge[0], 0) + 1
            counter[edge[1]] = counter.get(edge[1], 0) + 1

            if counter[edge[0]] == len(edges):
                return edge[0]
            if counter[edge[1]] == len(edges):
                return edge[1]
