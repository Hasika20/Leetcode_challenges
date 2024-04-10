class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        queue=deque()
        for i in range(n):
            queue.append(i)
        deck.sort()
        output=[0]*n
        for i in deck:
            output[queue.popleft()]=i
            if queue:
                queue.append(queue.popleft())
        return output