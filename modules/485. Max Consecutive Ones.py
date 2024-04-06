class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if (len(nums) == 1):
            return(nums[0])

        if not (1 < len(nums) <= 10 ** 5):
            return 0

        if not (0 in nums):
            return len(nums)

        consecutive_length = nums[0]
        max_length = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                consecutive_length = 0

            if (nums[i] == 1):
                consecutive_length += 1

            if (consecutive_length > max_length):
                max_length = consecutive_length

        return max_length


def main():
    nums = [1]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums=nums)
    print(result)

    #passed 61% speed 76% memory
main()