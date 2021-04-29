class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        prev_res = self.countAndSay(n-1)
        count, res = 1, []
        for i in range(1, len(prev_res)+1):
            if i<len(prev_res) and prev_res[i] == prev_res[i-1]:
                count += 1
            else:
                res.append(str(count))
                res.append(str(prev_res[i-1]))
                count = 1
        return "".join(res)
            