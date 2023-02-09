#
# Based on Code-wars kata:
# https://www.codewars.com/kata/511f11d355fe575d2c000001/python
#
class TwoOldestAges:
    # Gets two oldest ages from given array of ages
    def two_oldest_ages(self, ages):
        if ages is None or len(ages) < 2:
            return []
        ages.sort()
        return ages[-2:]
