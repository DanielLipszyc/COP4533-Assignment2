# COP4533-Assignment2

### Team Members

Daniel Lipszyc - 32328471

### Requirements
Language: Python 3.14.x (Should run on any 3.x)

### Build/Compilation Instructions
1. Clone the Repository

To run cache miss simulations:
1. Create a .in file that matches the input format.
2. Run it like this:

```bash
python3 src/cache.py tests/test1.in > tests/test1.out
```
### Written Component
Question 1: Files in /tests directory; named empirical(1-3).in

| Input File      | k | m   | FIFO | LRU | OPTFF |
|-----------------|---|-----|------|-----|-------|
| Emprirical 1    | 4 | 75  | 25   | 27  | 14    |
| Emprirical 2    | 3 | 80  | 34   | 29  | 21    |
| Emprirical 3    | 2 | 62  | 39   | 41  | 29    |

OPTFF has the fewest misses in each example, as it is optimal. 
As for LRU vs. FIFO, sometimes FIFO has more misses, sometimes LRU. It depends on how the requests are incoming.

Question2:

Since OPTFF is optimal, every sequence will be at least as good if not better than LRU and FIFO, with most being better.
Here is a simple one: 1 3 2 3 5 4 1 2 3
OPTFF misses: 6
LRU misses: 8
FIFO misses: 8

Question 3:

To prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence, we will use the exchange argument.
Let S be the cache for OPTFF and A the one for A.
If A always makes the same evicition calls as S, then S is optimal as they will have the same miss count. Anytime A makes a different eviction than S, with the caches being the same until this point, we make a new schedule called A', that evicted the same item as S, but everything else is as it was in A. So lets say that S evicted 1 and A evicted 2, we would make A' in which it evicted 1. We must show that this new schedule A' has the same/less misses as the original A. 

After the swap, A has 1 in cache but not 2, and A' has 2 in cache but not 1. Since S evicted 1 because it was the farthest in the future, that means 2 will be needed before 1. So when 2 gets requested, A misses because it doesn't have 2 anymore, but A' hits because it kept 2. At that point we can make the caches the same again, and A' ended up with one less miss. If 2 is never requested again, then it doesn't matter which one we evicted so the swap doesn't hurt anything. Either way, A' has the same or fewer misses than A.

Anytime there is a difference in evictions, we repeat the process, and by the end A will be the same as S. Therefore, the number of misses for OPTFF is no larger than ( A ) for any sequence.
