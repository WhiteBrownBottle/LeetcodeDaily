class Solution:
    def generate(self, numRows: int):
        res = []
        for i in range(1, numRows+1):
            if i == 1:
                tmp = [1]
                res.append(tmp)
            elif i == 2:
                tmp = [1, 1]
                res.append(tmp)
            else:
                before = res[i-2]
                tmp =[]
                for j in range(0, i):
                    if j == 0 or j == i-1:
                        tmp.append(1)
                    else:
                        tmp.append(before[j]+before[j-1])
                res.append(tmp)
        return res


if __name__ == '__main__':
    sol = Solution()
    output = sol.generate(5)
    print(output)