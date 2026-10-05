class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict, deque
        patterns = defaultdict(list)

        queue = deque([beginWord])
        visited = {beginWord}
        count = 1

        # build the pattern hashmap
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                patterns[pattern].append(word)
        # bfs
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return count
                #generate pattern for current word
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]

                    for neighbor in patterns[pattern]:
                        if neighbor in visited:
                            continue
                        
                        visited.add(neighbor)
                        queue.append(neighbor)
            count += 1
        
        return 0

