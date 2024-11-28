# Longest Compound Word Finder

The Solution identifies the **longest** and **second-longest compound words** from a given list of words. A compound word is a word composed of two or more smaller words that exist independently in the input dataset. The implementation uses a **Trie** data structure to efficiently store and search prefixes, optimizing the process of identifying compound words.

## Approach

1. **Data Structure: Trie**  
   A Trie is used to store all the input words, allowing for efficient prefix matching and word validation. Each node in the Trie represents a character, and terminal nodes mark the end of valid words.

2. **Build Phase**  
   - The words are read from the input file line by line.
   - For each word, potential prefixes are extracted using the `getPrefixes` method of the Trie.
   - For every prefix found, the remaining suffix is added to a queue along with the original word.
   - The word is then inserted into the Trie for future lookups.

3. **Processing Queue**  
   - Each entry in the queue is processed by checking if the suffix is a valid word in the Trie.
   - If the suffix forms a valid word and the current word's length exceeds the longest compound word found so far, update the longest and second-longest compound words.
   - If not, potential prefixes of the suffix are extracted, and new entries are added to the queue for further exploration.

4. **Output**  
   The longest and second-longest compound words are returned along with the computation time.

This approach ensures efficient handling of large datasets, leveraging the Trie's hierarchical structure and breadth-first exploration.