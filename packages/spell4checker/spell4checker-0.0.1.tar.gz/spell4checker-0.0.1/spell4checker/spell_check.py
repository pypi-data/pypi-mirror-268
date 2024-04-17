import csv
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def build_prefix_tree(file_path):
    trie = Trie()
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            word = row['Word'].strip().lower()
            trie.insert(word)
    return trie

def longest_common_subsequence(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

def spell_checker(input_word, trie):
    corrected = []
    def dfs(node, prefix):
        if node.is_end_of_word:
            lcs_length = longest_common_subsequence(input_word, prefix)
            edit_dist = edit_distance(input_word, prefix)
            corrected.append((prefix, lcs_length, edit_dist))
        for char, child_node in node.children.items():
            dfs(child_node, prefix + char)
    
    dfs(trie.root, "")
    corrected.sort(key=lambda x: (-x[1], x[2]))
    return corrected[0][0]