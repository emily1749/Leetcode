class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # if len(wordss)<2: return
        adj_list = defaultdict(list)
        indegree = Counter({c : 0 for word in words for c in word})
        
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            a, b = 0, 0
            while a<len(word1) and b<len(word2):
                c1, c2 = word1[a], word2[b]
                if c1==c2:
                    a+=1
                    b+=1
                    continue
                adj_list[c1].append(c2)
                if c2 not in indegree:
                    indegree[c2] = 0
                if c1 not in indegree:
                    indegree[c1] = 0
                indegree[c2] += 1
                break
            print(a)
            print(len(word1))
            print(len(word2))
            print(len(words))
            if a == len(word2) and len(word1)>=a and len(word2) < len(word1) and len(words) == 2: 
                return ""
        
        print(adj_list)
        # print(indegree)
        
        queue = collections.deque([c for c in indegree if indegree[c]==0])
        result = ''
        # print(queue)
        while queue:
            current = queue.popleft()
            # print(current)
            result += current
            indegree[current] -= 1
            for letter in adj_list[current]:
                indegree[letter] -= 1
                if indegree[letter] == 0:
                    queue.append(letter)
        if len(result) != len(adj_list): return ""
        
        return result
        