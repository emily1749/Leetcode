class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        adj_list = defaultdict(list)
        
        for i in range(len(accounts)):
            account = accounts[i]
            if len(account) == 2: adj_list[account[1]] = []
            for i in range(2, len(account)):
                adj_list[account[i]].append(account[i-1])
                adj_list[account[i-1]].append(account[i])
        
        seen, curr = set(), []
        def dfs(node):
            seen.add(node)
            curr.append(node)
            for neighbor in adj_list[node]:
                if neighbor in seen: continue
                dfs(neighbor)
            
        result = []
        for account in accounts:
            if account[1] not in seen:
                curr = []
                dfs(account[1])
                curr = [account[0]] + sorted(curr)
                result.append(curr)
        return result
            
                
            
            
#         accounts_idx = 0
#         # result_idx = 0
#         email_to_idx = {}
#         result = []
#         while accounts_idx < len(accounts):
#             account = accounts[accounts_idx]
#             for i in range(1, len(account)):
#                 email = account[i]
#                 if email in email_to_idx:
#                     #already inside
#                     idx = email_to_idx[email]
#                     for j in range(1, len(account)):
#                         if account[j] not in email_to_idx:
#                             result[idx].append(account[j])
            
#                     continue
#                     #continue
#             result.append(account)
#             result_idx = len(result) - 1
#             for i in range(1, len(account)):
#                 email_to_idx[account[i]] = result_idx