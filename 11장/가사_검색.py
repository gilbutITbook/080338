class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        current = self.head

        for char in string:
            current.count += 1
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

    def starts_with(self, prefix):
        current = self.head
        result = 0

        for char in prefix:
            if char == '?': break
            if char in current.children: current = current.children[char]
            else: return 0

        return current.count

def solution(words, queries):
    answer = []
    tries = {}
    reverse_tries = {}

    for word in words:
        size = len(word)
        if size not in tries:
            tries[size] = Trie()
            reverse_tries[size] = Trie()
            
        tries[size].insert(word)
        reverse_tries[size].insert(word[::-1])

    for query in queries:
        if len(query) in tries:
            if query[0] != '?':
                trie = tries[len(query)]
                answer.append(trie.starts_with(query))
            else:
                trie = reverse_tries[len(query)]
                answer.append(trie.starts_with(query[::-1]))
        else: answer.append(0)

    return answer

