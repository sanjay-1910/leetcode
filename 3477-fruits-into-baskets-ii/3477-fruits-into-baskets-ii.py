class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n  # To track which baskets have been used
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True  # Mark basket as used
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced