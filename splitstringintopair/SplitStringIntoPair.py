#
# Based on Code-wars kata:
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python
#
class SplitStringIntoPair:
    # Splits given string into pairs. If original string has odd length, it should be completed with _ character
    def split(self, str):
        if str is None or len(str) < 1:
            return []

        if len(str) % 2 != 0:
            str += "_"
        result = ["" for x in range(len(str) // 2)]

        for i in range(len(result)):
            result[i] = str[i * 2: i * 2 + 2]

        return result
