class Solution:
    def maximumSwap(self, num: int) -> int:
        if not (0 <= num <= 10 ** 8):
            return 0

        int_array = [int(num) for num in list(str(num))]
        max_val = max(int_array)
        count = int_array.count(max_val)

        if (count == len(int_array)):
            return num
        
        if(int_array[0] != max_val):
            rev = int_array[::-1]
            index = len(int_array) - 1 - rev.index(max_val)
            int_array[0], int_array[index] = int_array[index], int_array[0]
        else:
            for i in range(1, len(int_array) - 1):
                if (int_array[i] != max_val):
                    new_array = int_array[i:]
                    new_max = max(new_array)
                    rev = new_array[::-1]
                    index = len(new_array) - 1 - rev.index(new_max)
                    int_array[index + i], int_array[i], = int_array[i], int_array[index + i]
                    break

        return(int(''.join(str(i) for i in int_array)))

    def maximumSwap2(self, num: int) -> int:
        if not (0 <= num <= 10 ** 8):
            return 0

        def swap(index, int_array):
            if index >= len(int_array):
                return int(''.join(map(str, int_array)))

            max_val = max(int_array[index:])
            max_index = len(int_array) - 1 - int_array[::-1].index(max_val)

            if max_val != int_array[index]:
                int_array[index], int_array[max_index] = int_array[max_index], int_array[index]
                return int(''.join(map(str, int_array)))
            
            return swap(index + 1, int_array)

        int_array = [int(digit) for digit in str(num)]
        return swap(0, int_array)


def main():
    num = 98368
    solution = Solution()
    result = solution.maximumSwap2(num=num)
    print(result)

    #solved linear with 109/112 (97%+) passed in maximumSwap

    #solved recursive in maximumSwap2
    # passed with 32% speed and 99% memory

main()