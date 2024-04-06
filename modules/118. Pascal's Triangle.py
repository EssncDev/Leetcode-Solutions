class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        return_array = []
        if not(0 < numRows < 31):
            return return_array

        if (numRows == 1):
            return [[1]]

        if (numRows == 2):
            return [[1], [1,1]]

        return_array = [[1],[1,1]]
        for i in range(2, numRows):
            current_array = [1]
            last_array = return_array[len(return_array)-1]
            
            for elmt in range(0, len(last_array)-1):
                current_array.append(last_array[elmt] + last_array[elmt + 1])

            current_array.append(1)
            return_array.append(current_array)

        return(return_array)
            

def main():
    num = 5
    solution = Solution()
    result = solution.generate(numRows=num)

    for x in result:
        print(x)

    #passed with 84% in speed and 58% in memory

main()