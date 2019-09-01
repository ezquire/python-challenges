import timeit
import heapq
from collections import Counter

def topKFrequentHeap(words, k):
    dic = Counter(words)
    wordList = list(dic.keys())
    heapq.heapify(wordList)
    return heapq.nlargest(k, wordList, key = lambda word: dic[word])

def topKFrequentSort(words, k):
    dic = Counter(words)
    wordList = list(dic.keys())
    return sorted(wordList, key = lambda word: (-dic[word], word))[:k]

def heap_time():
    SETUP = ''' 
from collections import Counter
import heapq
'''
    TEST = '''
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
def topKFrequentHeap(words, k):
    dic = Counter(words)
    wordList = list(dic.keys())
    heapq.heapify(wordList)
    return heapq.nlargest(k, wordList, key = lambda word: dic[word])
topKFrequentHeap(words, k)
'''
    return timeit.timeit(setup = SETUP, stmt = TEST, number=100000)


def sort_time():
    SETUP = ''' 
from collections import Counter
'''
    TEST = '''
def topKFrequentSort(words, k):
    dic = Counter(words)
    wordList = list(dic.keys())
    return sorted(wordList, key = lambda word: (-dic[word], word))[:k]
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
topKFrequentSort(words, k)
'''
    return timeit.timeit(setup = SETUP, stmt = TEST, number=100000)

print("Heap Time:", heap_time())
print("Sort Time:", sort_time())
