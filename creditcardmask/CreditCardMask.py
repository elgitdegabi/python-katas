#
# Based on Code-wars kata:
# https://www.codewars.com/kata/5412509bd436bd33920011bc/solutions/python
#
class CreditCardMask:
    # Generates a mask for given str except last 4 characters
    def maskify(self, str):
        if str is None or len(str) <= 4:
            return str
        mask = ""
        for i in range(len(str) - 4):
            mask += "#"
        return mask + str[len(str) - 4:len(str)]
