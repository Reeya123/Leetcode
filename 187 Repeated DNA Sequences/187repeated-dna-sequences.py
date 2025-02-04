class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        charset = set()
        repeatedset = set()

        for index in range(len(s) - 9):
            substring = s[ index: index + 10]

            if substring in charset:
                repeatedset.add(substring)

            else:
                charset.add(substring)

        return list(repeatedset)


        