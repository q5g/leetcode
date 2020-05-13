class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        min_length = len(s)
        output = ''
        long = {}  # {char: [index1, index2, ...]}

        short = {}  # {char:count}
        for c in t:
            if c not in short.keys():
                short[c] = 1
            else:
                short[c] += 1

        for i, c in enumerate(s):
            if c not in short.keys():
                continue

            if c not in long.keys():
                long[c] = [i]
            else:
                if len(long[c]) == short[c]: # "bba", "ab"
                    long[c].append(i)
                    long[c] = long[c][1:]
                else:
                    long[c].append(i)
            print(long)
            if self.contain(long, short):
                start = self.find_first(long, i)
                if min_length >= i - start + 1:
                    min_length = i - start + 1
                    output = s[start:i + 1]
        return output

    def contain(self, long: dict, short: dict) -> bool:
        if len(long.keys()) < len(short.keys()):
            return False

        for k, v in short.items():
            if len(long[k]) != v:
                return False
        return True

    def find_first(self, d: dict, i: int) -> int:
        first = i
        for l in d.values():
            first = min(first, l[0])
        return first

def main():
    solution = Solution()
    print(solution.minWindow('a', 'a'))
    print(solution.minWindow('ab', 'b'))
    print(solution.minWindow('bba', 'ab'))

if __name__ == "__main__":
    main()