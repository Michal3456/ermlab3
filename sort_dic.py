import operator
from Vector import Vector


class SortDic():
    @staticmethod
    def sort_dic(__table_count__: Vector):
        """For refinement."""
        __sorted_d__ = sorted(__table_count__.items(), key=operator.itemgetter(1))
