class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # pos ast collides with neg ast; -> <-
        stk = []
        for ast in asteroids:
            while stk and stk[-1] > 0 and ast < 0:
                if stk[-1] + ast < 0: # prev dies
                    stk.pop()
                elif stk[-1] + ast > 0: # ast dies
                    ast = 0
                else: # both dies
                    stk.pop()
                    ast = 0
            if ast:
                stk.append(ast)

        return stk