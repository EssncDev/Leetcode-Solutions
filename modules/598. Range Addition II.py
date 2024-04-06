class Solution:
    def first_solution(self, m: int, n: int, ops: list[list[int]]) -> int:
        M = [[0 for j in range(n)] for i in range(m)]
        heighest_num = 0
        heighest_num_counter = 0

        if not(0 < m and n <= 4 * 10 ** 4):
            return (m * n)

        if not(0 < len(ops) <= 10 ** 4):
            return (m * n)

        for i in range(0, len(ops)):
            if not(len(ops[i]) == 2):
                continue

            x = ops[i][0]
            y = ops[i][1]
            if not(0 < x <= m):
                continue
            
            if not(0 < y <= n):
                continue
            
            for j in range(0, y):
                for k in range(0, x):
                    M[j][k] += 1

                    if (M[j][k] > heighest_num):
                        heighest_num = M[j][k]
                        heighest_num_counter = 0

                    if (M[j][k] == heighest_num):
                        heighest_num_counter += 1

        return(heighest_num_counter)

    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_y = m
        min_x = n

        for y, x in ops:
            min_y = min(min_y, y)
            min_x = min(min_x, x)

        return min_x * min_y
        

def main():
    m = 3
    n = 3
    ops = [[2,2],[2,3]]

    solution = Solution()
    print(solution.first_solution(m=m, n=n, ops=ops))
    print(solution.maxCount(m=m, n=n, ops=ops))

main()