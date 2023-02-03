#
# Based on Code-wars kata:
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/python
#
class ConcatenateConsecutiveStrings:
    # Returns concatenated k strings of length k or grater
    def consecutive_string(self, strarr, k):
        result = "";

        if len(strarr) > 0 and 0 < k < len(strarr):
            for i in range(len(strarr) - k + 1):
                current = ""
                j = i
                for j in range(i, (i + k)):
                    current += strarr[j]
                if len(current) > len(result):
                    result = current
        return result
