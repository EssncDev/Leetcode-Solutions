class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not(1 <= len(word) <= 100):
            return False
        
        current_result = []
        for letter in word:
            current_result.append((letter == letter.lower()))
        
        if (current_result[0] == False):
            remaining = current_result[1:]
            if (all(c == remaining[0] for c in remaining)):
                return True

        return(all(c == current_result[0] for c in current_result))


def main():
    word = "LeeTcode"
    solution = Solution()
    result = solution.detectCapitalUse(word=word)
    print(result)

    #passed 84% speed and 89% in memory
main()