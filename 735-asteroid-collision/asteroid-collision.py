class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # Process only when collision is possible
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:  # stack top is smaller, it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:  # both are equal, both explode
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
                
            
            
