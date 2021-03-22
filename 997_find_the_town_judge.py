class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        adj_list = defaultdict(set)
        for person in trust:
            adj_list[person[0]].add(person[1])
        trusts_nobody = []
        for i in range(1, N+1):
            if i not in adj_list:
                trusts_nobody.append(i)
        if not len(trusts_nobody) == 1:
            return -1
        judge = trusts_nobody[0]
        for node in adj_list:
            if judge not in adj_list[node]:
                return -1
        return judge