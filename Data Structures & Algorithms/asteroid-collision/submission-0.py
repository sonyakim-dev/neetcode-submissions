class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # pos ast collides with neg ast!!!
        # neg ast on the 0th position will never collide
        stk = []

        for ast in asteroids:
            while stk and stk[-1] > 0 and ast < 0:
                diff = stk[-1] + ast
                if diff < 0: # ast survive
                    stk.pop()
                elif diff > 0: # stk[-1] survive
                    ast = 0
                else: # both die
                    stk.pop()
                    ast = 0
            if ast:
                stk.append(ast)

        return stk