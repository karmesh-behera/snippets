
import heapq




def runningMedian(stream):
    min_heap = []
    max_heap = []
    result = []

    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for x in stream:
        heapq.heappush(max_heap, -1*heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        result.append(0.5*(min_heap[0] + (-1*max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])
    return result



def main():
    stream = [1, 0, 3, 5, 2, 0, 1]
    print(runningMedian(stream))

if __name__ == "__main__":
    main()