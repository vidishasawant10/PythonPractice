class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = ""

        for i in s:
            stri = s.strip(" ")
            spl = stri.split(" ")
            a = spl[-1]
            return len(a)

