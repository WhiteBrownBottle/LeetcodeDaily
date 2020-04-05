class Solution:
    def readBinaryWatch(self, num: int) -> list:
        return [f"{h}:{m:02d}" for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]


