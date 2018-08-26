"""

"""
import queue
def generateNeighbors(word, wordList):
    neighbors = []
    for w in wordList:
        diff = 0
        for i in range(len(word)):
            if w[i] != word[i]:
                diff += 1
        if diff <= 1:
            neighbors.append(w)

    return neighbors

    """
    make a new word with each combination using the entire alphabet
    check if its in wordlist 
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            new_word = word[:i] + letter + word[(i+1):]
            if new_word in wordList:
                neighbors.append(new_word)

        return neighbors
    """


def wordLadder(beginWord, endWord, wordList):

    q = queue.Queue()
    q.put((beginWord, 1))

    # keeps track of what has already been visited so we dont get
    # stuck in a loop
    visited = {}

    while not q.empty():
        # also keeps track of the number of words it takes to get there
        (word, steps) = q.get()
        visited[word] = True
        for neighbor in generateNeighbors(word, wordList):
            if neighbor == endWord:
                return steps + 1
            if neighbor not in visited:
                q.put((neighbor, steps + 1))
    return 0

print(generateNeighbors('dot', ['hot', 'dog', 'lit', 'lot']))
print(wordLadder('hot', 'dot', ['hit', 'dip', 'dot']))
print(wordLadder('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(wordLadder('hit', 'cog', ["hot","dot","dog","lot","log"]))
