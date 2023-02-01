#
# Based on Code-wars kata:
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/python
#
class EvenOrOdd:
    # Returns if given number is even or odd
    def even_or_odd(self, number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
