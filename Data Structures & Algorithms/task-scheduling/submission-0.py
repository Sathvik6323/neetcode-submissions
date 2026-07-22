class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        t=0
        q=deque()

        while maxheap or q:
            t+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,t+n])
            
            if q and q[0][1]==t:
                heapq.heappush(maxheap,q.popleft()[0])
        
        return t

        