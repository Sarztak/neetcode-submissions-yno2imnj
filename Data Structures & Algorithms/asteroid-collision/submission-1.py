class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = [] 

        def sign(n):
            return 'p' if n > 0 else 'n'

        for i in range(n):

            has_survived = True 

            while stack and sign(stack[-1]) == 'p' and sign(asteroids[i]) == 'n' and abs(stack[-1]) <= abs(asteroids[i]):
                x = stack.pop()
                if abs(x) == abs(asteroids[i]):
                    has_survived = False
                    break

            if not has_survived or (stack and sign(stack[-1]) == 'p' and sign(asteroids[i]) == 'n' and abs(stack[-1]) > abs(asteroids[i])):
                continue
            stack.append(asteroids[i])
        
        return stack