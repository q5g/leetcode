from typing import List

class Solution:
    num2letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        result = ['']
        for d in digits:
            letters = self.num2letter[d]
            length = len(result)
            for i in range(length):
                r = result[i]
                for l in letters:
                    result.append(r + l)
            result = result[length:]
        return result

def main():
    solution = Solution()
    input = '23'
    print(solution.letterCombinations(input))


if __name__ == "__main__":
    main()