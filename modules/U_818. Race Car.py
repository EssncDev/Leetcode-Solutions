import time as t

class Solution:
    def racecar(self, target: int) -> int:
        self.pos = 0
        self.speed = 1
        self.steps = ''

        def a():
            self.pos += self.speed
            self.speed *= 2
            self.steps += 'a'
        
        def r():
            if (self.speed > 0):
                self.speed = -1
            else:
                self.speed = 1
            self.steps += 'r'

        while (self.pos != target):
            if (self.pos < target):
                if(self.pos + self.speed > target):
                    r()

                if (self.speed < 0):
                    r()
                else:
                    a()

            if (self.pos > target):
                if (self.speed > 0):
                    r()
                else:
                    a()
                
        return(len(self.steps))
            



def main():
    target = 64
    solution = Solution()
    result = solution.racecar(target=target)
    print('result:', result)

main()