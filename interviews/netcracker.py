# Write python decorator to return exceptions from the functions so that user can get the the exception withtout handling it.

def manage_exceptions(func):

    def wrapper(*args, **kwargs):
        try:
            a = kwargs.get('a')
            f = kwargs.get('func')
            func(a, f)
        except Exception as err:
            return str(err)
        
    return wrapper


@manage_exceptions
def error_function(*args, **kwargs):
    f = kwargs.get('func')
    10 / 0

result = error_function()
print(result)


"""
Problem Statement: Word Ladder
Given two words, beginWord and endWord, and a list of words (wordList), the goal is to transform beginWord into endWord by changing only one letter at a time. 
Each intermediate word must exist in the wordList. The transformation sequence must have the minimum possible steps.

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Output: 5
Explanation: The shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which has 5 words.

Implementation Idea:
This is typically solved using Breadth-First Search (BFS):

Treat each word as a node in a graph.
An edge exists between two nodes if their words differ by exactly one letter.
Use BFS to find the shortest path from beginWord to endWord.
Here’s a Python implementation:
"""

from collections import deque

def word_ladder_length(beginWord, endWord, wordList):
    wordList = set(wordList)  # Convert list to set for O(1) lookups.
    if endWord not in wordList:
        return 0

    # BFS Initialization
    queue = deque([(beginWord, 1)])  # (current_word, current_depth)
    
    while queue:
        word, steps = queue.popleft()
        
        # Check all possible single-letter transformations
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                
                if next_word == endWord:
                    return steps + 1  # Found the shortest path
                
                if next_word in wordList:
                    wordList.remove(next_word)  # Mark as visited
                    queue.append((next_word, steps + 1))
    
    return 0  # No transformation found

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(word_ladder_length(beginWord, endWord, wordList))  # Output: 5


