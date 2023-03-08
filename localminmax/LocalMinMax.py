#
# Based on Google interview challenge
#
class LocalMinMax:
    # Gets local min and max values from given int array
    def get_local_min_max(self, list):
        if list is None or len(list) < 1:
            return [0, 0]
        else:
            return [min(list), max(list)]

    # Gets local min and max values from given int array
    def get_local_min_max_alternative(self, list):
        if list is None or len(list) < 1:
            return [0, 0]
        else:
            sorted_list = sorted(list)
            return [sorted_list[0], sorted_list[len(sorted_list) - 1]]
