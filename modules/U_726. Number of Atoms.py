class Solution:
    def countOfAtoms(self, formula: str) -> str:
        if not "(" in formula:
            return(formula)

        store_dict = {}
        for char in formula:
            if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                store_dict[char] = 1
                
        copy = formula
        array = []
        while "(" in copy:
            rev = copy[::-1]
            copy = copy[copy.index('(') + 1:len(copy) - rev.index(')') - 1]
            array.append(copy)

        print(array)

        copy = formula
        for elmt in range(0,len(array)):
            index = formula.index(array[elmt])
            sub =  copy[index + len(array[elmt]) + 1:]

            for char in array[elmt]:
                if (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                    store_dict[char] *= sub

        print(store_dict)

        


def main():
    word = "K4(ON(SO3)2)2"
    word = "Mg(OH)2"
    #word = "H2O"
    solution = Solution()
    result = solution.countOfAtoms(formula=word)
    print(result)

main()