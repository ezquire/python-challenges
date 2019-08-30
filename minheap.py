class minheap:
    def __init__(self, arr):
        self.heap = arr
        self.heapify()

    def heappush(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap) - 1)

    def heappop(self):
        lastelt = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            _siftup(0)
        else:
            returnitem = lastelt
        return returnitem

    def heapify(self):
        n = len(self.heap)
        for i in range((n - 2)//2, -1 ,-1):
            self._siftup(i)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
                      
    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)

    def peek(self):
        return self.heap[0]

arr = [21, 1, 45, 78, 3, 5]
heap = minheap(arr)
print(heap.heap)
