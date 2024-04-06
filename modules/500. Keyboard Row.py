class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result_array = []

        if(len(words) > 20):
            return result_array
        
        for word in words:
            current_result = []
            if not (1 <= len(word) <= 100):
                continue

            for i in word:
                letter = i.lower()
                for row in range(0, len(keyboard)):
                    if (letter in keyboard[row]):
                        current_result.append(row)

            if(all(c == current_result[0] for c in current_result)):
                result_array.append(word)                

        return result_array




def main():
    words = ["Hello","Alaska","Dad","Peace"]
    words = ["omk"]
    words = ["adsdf","sfd"]
    solution = Solution()
    result = solution.findWords(words=words)
    print(result)

    #passed 54% speed and 83% memory
main()