#
# Based on Interview challenge:
# Calculate Nth Fibonacci number and optimize your solution to support "big numbers"
#
class FibonacciNumber:
    MAX_SUPPORTED_VALUE = 99

    # Returns fibonacci Nth number
    def calculate(self, k):
        if k < 1 or k > FibonacciNumber.MAX_SUPPORTED_VALUE:
            return 0
        if k <= 2:
            return 1
        return FibonacciNumber.calculate(self, k - 1) + FibonacciNumber.calculate(self, k - 2)

    # Returns fibonacci Nth number using memoization
    def calculate_with_memoization(self, k, custom_cache):
        if k < 1 or k > FibonacciNumber.MAX_SUPPORTED_VALUE:
            return 0
        if k in custom_cache:
            return custom_cache[k]
        if k <= 2:
            return 1

        before_previous = FibonacciNumber.calculate_with_memoization(self, k - 2, custom_cache)
        previous = FibonacciNumber.calculate_with_memoization(self, k - 1, custom_cache)
        current = before_previous + previous

        custom_cache[k] = current;

        return current
