class Solution:
    def romanToInt(self, s: str):
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == 'I':
                s_list[i] = 1
            elif s_list[i] == 'V':
                s_list[i] = 5
            elif s_list[i] == 'X':
                s_list[i] = 10
            elif s_list[i] == 'L':
                s_list[i] = 50
            elif s_list[i] == 'C':
                s_list[i] = 100
            elif s_list[i] == 'D':
                s_list[i] = 500
            elif s_list[i] == 'M':
                s_list[i] = 1000
            else:
                return None
        len_s = len(s_list)
        if len_s >= 2:
            if s_list[0] < s_list[1]:
                s_list[0] = 0 - s_list[0]
            for j in range(1, len_s - 1):
                if s_list[j] < s_list[j - 1] and s_list[j] < s_list[j + 1]:
                    temp = s_list[j]
                    s_list[j] = 0 - temp
        return sum(s_list)





if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("III"))


#1000 100 1000 10 100 10 1 5