from add_space import AddSpace
import operator


class SortingWriteToFile():
    @staticmethod
    def write_to_file(path_to_file_obwody, __table_count__):
        """Adding a sorted dictionary to the analysis file."""
        with open(path_to_file_obwody, 'a') as files3:
            __sorted_d__ = sorted(__table_count__.items(), key=operator.itemgetter(1))
            __sorted_d__.pop()
            __sorted_d__.reverse()
            for key, value in __sorted_d__:
                sum = ["Count: %d %s Word: %r\n" % (value, AddSpace.add_space(value), key)]

                files3.writelines(sum)
