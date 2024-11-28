# Solution.py
import Trie as T
from collections import deque
import time

class Solution:
    def __init__(self) -> None:
        self.trie = T.Trie()
        self.queue = deque()

    def buildTrie(self, filePath: str = None) -> None:
        try:
            with open(filePath, mode='r') as f:
                for line in f:
                    word = line.rstrip('\n')
                    for prefix in self.trie.getPrefixes(word):
                        self.queue.append((word, word[len(prefix):]))
                    self.trie.insert(word)
        except:
            print("Error reading the file!")
            exit(0)
    
    def findLongestCompoundWords(self) -> tuple:
        longest_word = ''
        longest_length = 0
        second_longest = ''
        
        while self.queue:
            word, suffix = self.queue.popleft()
            if suffix in self.trie and len(word) > longest_length:
                second_longest, longest_word = longest_word, word
                longest_length = len(word)
            else:
                for prefix in self.trie.getPrefixes(suffix):
                    self.queue.append((word, suffix[len(prefix):]))

        return longest_word, second_longest

if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    sol.buildTrie("Input_02.txt") #Note please add the input file from here please
    first, second = sol.findLongestCompoundWords()
    end = time.time()
    print("Longest Compound Word:", first)
    print("Second Longest Compound Word:", second)
    print("Time taken:", str(end - start), "seconds")

