#
# Based on Geeks for geeks exercise:
# https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/1
#
class FibonacciElements:

    # Returns first K fibonacci elements
    def get_elements(self, k):
        if k < 1 or k > 84:
            return []
        else:
            result = [None] * k
            for i in range(k):
                if i < 2:
                    result[i] = 1
                else:
                    result[i] = result[i - 1] + result[i - 2]
            return result
