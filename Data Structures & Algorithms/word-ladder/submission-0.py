class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # iterate once through wordList, add 1 char diff words to neighbors dict
        # then bfs to find min distance between two
        # checking all paths? is that too inefficient?
        # nah prob not too inefficient, worst case we have max 9 edges per word * 100 words
        # and it would prob take a few hundred iterations, or maybe more
        # but not more than 900 ig
        # or in other words, max 100 bfs iterations, so not too bad

        # BUT if I've already visited a node I know I shouldn't visit it again - this is a longer path

        neighbors = {word: [] for word in wordList}
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i == j:
                    continue
                # check if 1 letter apart - we know they are same length
                differences = 0
                for l1, l2 in zip(wordList[i], wordList[j]):
                    if l1 != l2:
                        differences += 1
                if differences == 1:                  
                    neighbors[wordList[i]].append(wordList[j])

        print(neighbors)
        # Now, just BFS from starting word -> all it's neighbors (manually find),
        # then from all their neighbors and so on
        starting_words = []
        for word in wordList:
            differences = 0
            for l1, l2 in zip(beginWord, word):
                if l1 != l2:
                    differences += 1
            if differences == 1:
                starting_words.append(word)
                if word == endWord:
                    return 2

        distance = 2
        visited = set()
        while starting_words:
            print(starting_words)
            next_words = []
            for word in starting_words:
                for next_word in neighbors[word]:
                    if next_word == endWord:
                        return distance + 1
                    if next_word not in visited:
                        next_words.append(next_word)
                        visited.add(next_word)
            
            distance += 1
            starting_words = next_words



        return 0

