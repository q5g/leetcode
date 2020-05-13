class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        result = 0
        # inital whitespaces
        while str[i] == ' ':
            i += 1

        # first non-whitespace character is digit or plus/minus sign
        positive = True
        if str[i] in ['+', '-']:
            positive = False if str[i] == '-' else True
            i += 1
        while i < len(str) and ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            result = result * 10 + ord(str[i]) - ord('0')
            i += 1

        if positive:
            if result > 2147483647:
                return 2147483647
            else:
                return result
        else:
            if result > 2147483648:
                return -2147483648
            else:
                return -result

def main():
    solution = Solution()
    input = '   +-42'
    print(solution.myAtoi(input))


if __name__ == "__main__":
    main()