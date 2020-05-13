class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ''
        # row = 0
        i = 0
        while (i < len(s)):
            result += s[i]
            i += (numRows - 1) * 2

        # row = 1 ... numRows-2
        for row in range(1, numRows - 1):
            i = row
            while (i < len(s)):
                result += s[i]
                i += (numRows - 1 - row) * 2
                if (i < len(s)):
                    result += s[i]
                    i += row * 2
                else:
                    break

        # row = numRows - 1
        i = numRows - 1
        while (i < len(s)):
            result += s[i]
            i += (numRows - 1) * 2

        return result


def main():
    solution = Solution()
    s = 'PAYPALISHIRING'
    print(solution.convert(s, 1))
    print(solution.convert(s, 4))


if __name__ == "__main__":
    main()