import sys


def FIFO(capacity, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            pass
        else:
            misses += 1
            if len(cache) == capacity:
                cache.pop(0)
            cache.append(request)
    return misses


def LRU(capacity, requests):
    cache = []
    misses = 0

    for request in requests:
        if request in cache:
            cache.remove(request)
            cache.append(request)
        else:
            misses += 1
            if len(cache) == capacity:
                cache.pop(0)
            cache.append(request)
    return misses


def OPTFF(capacity, requests):
    cache = []
    misses = 0

    for i in range(len(requests)):
        request = requests[i]

        if request in cache:
            continue
        else:
            misses += 1
        if len(cache) < capacity:
            cache.append(request)
            
        else: 
            furthest = -1
            evict = cache[0]
            for item in cache:
                found = len(requests)
                for j in range(i + 1, len(requests)):
                    if requests[j] == item:
                        found = j
                        break
                if found > furthest:
                    furthest = found
                    evict = item
            cache.remove(evict)
            cache.append(request)
    return misses


if __name__ == "__main__":
    file = open(sys.argv[1])
    first_line = file.readline().split()
    k = int(first_line[0])
    m = int(first_line[1])
    requests = list(map(int, file.readline().split()))
    file.close()

    print("FIFO  : " + str(FIFO(k, requests)))
    print("LRU   : " + str(LRU(k, requests)))
    print("OPTFF : " + str(OPTFF(k, requests)))