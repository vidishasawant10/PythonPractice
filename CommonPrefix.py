from _ast import List


class CommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if len(strs) == 0:
            return res
        if len(strs) == 1:
            return (strs[0])

        pref = strs[0]

        for i in range(len(pref)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res