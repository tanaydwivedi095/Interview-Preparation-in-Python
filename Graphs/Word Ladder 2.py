from collections import defaultdict
from collections import deque

def wordLadderLength(startWord, targetWord, wordList):
    if endWord not in wordList:
        return 0
    sequence = []
    nei=defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern=word[:j]+"*"+word[j+1:]
            nei[pattern].append(word)
    visit=set([beginWord])
    q=deque([beginWord])
    count=1
    while q:
        sequence.append(q[0])
        for i in range(len(q)):
            word=q.popleft()
            if word==endWord:
                return sequence
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                for neiword in nei[pattern]:
                    if neiword not in visit:
                        visit.add(neiword)
                        q.append(neiword)
        count+=1
    return []

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dog","dot","lot","log","cog"]
    print(wordLadderLength(beginWord, endWord, wordList))
