from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        count = 0
        ileft, iright, jtop, jbottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        i, j = 0, 0
        spiral = []

        while count < len(matrix) * len(matrix[0]):
            if i == ileft and j == jtop:
                while i <= iright:
                    spiral.append(matrix[j][i])
                    i += 1
                    count += 1
                i -= 1
                jtop += 1
                j = jtop
            elif i == iright and j == jtop:
                while j <= jbottom:
                    spiral.append(matrix[j][i])
                    j += 1
                    count += 1
                j -= 1
                iright -= 1
                i = iright
            elif i == iright and j == jbottom:
                while i >= ileft:
                    spiral.append(matrix[j][i])
                    i -= 1
                    count += 1
                i += 1
                jbottom -= 1
                j = jbottom
            elif i == ileft and j == jbottom:
                if jtop == jbottom:
                    continue
                while j >= jtop:
                    spiral.append(matrix[j][i])
                    j -= 1
                    count += 1
                j += 1
                ileft += 1
                i = ileft

        return spiral

def main():
    solution = Solution()
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12], [13, 14, 15, 16]]))
    print(solution.spiralOrder([[0], [1], [0]]))
    print(solution.spiralOrder([]))


if __name__ == "__main__":
    main()