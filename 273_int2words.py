class Solution:
    digit2word = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety'
    }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        sep = ['Billion', 'Million', 'Thousand', '']
        sep_num = [1000000000, 1000000, 1000, 1]
        result = ''
        for s, n in zip(sep, sep_num):
            q = num // n
            num = num % n
            if q == 0:
                continue
            else:
                result = ' '.join([result, self.n2w(q), s])
        return result.strip()

    # convert for num < 1000
    def n2w(self, num: int) -> str:
        result = None
        hundreds = num // 100
        if hundreds > 0:
            result = ' '.join([self.digit2word[hundreds], 'Hundred'])
        num = num % 100
        if num == 0:
            tail = ''
        elif num <= 20:
            tail = self.digit2word[num]
        elif num % 10 == 0:
            tail = self.digit2word[num]
        else:
            tens = (num // 10) * 10
            ones = num % 10
            tail = ' '.join([self.digit2word[tens], self.digit2word[ones]])

        if result:
            result = ' '.join([result, tail])
        else:
            result = tail
        return result.strip()


def main():
    solution = Solution()
    input = 30
    print(solution.numberToWords(input))


if __name__ == "__main__":
    main()