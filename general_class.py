from line_split import LineSplit
from write_to_file import SortingWriteToFile


class GeneralClass:
    def read_metod_write(path_to_file_book: str, path_to_file_obwody: str):
        '''reading the book and recording the results based on the book.'''
        with open(path_to_file_book) as files:
            _table = []
            __table_count__ = {}
            line2 = []

            LineSplit.line_split(line2, files, __table_count__, _table)
            # for line in files:
            #    line2 = line.split()
            # for count, elem in enumerate(line2):
            #    print(count, elem)
            # print(line2)

        #                   for word in line2:
        #                       if word not in _table:
        #                           _table.append(word)
        #                           #print(_table[i])
        #                           i=i+1
        #                           __table_count__[word]=1
        #                       else:
        #                           __table_count__[word]=__table_count__[word]+1
        #                           _table_count[word]=_table_count[word]+1

        # for element in _table:
        #    print(element)
        #            with open(path_to_file_obwody, 'a') as files3:
        #                    for element in __table_count__:
        #                        #print(element)
        #                        #print(_table_count[element])
        #                        a=__table_count__[element]
        #                        sum = ["Ilość: %d %s Słowo: %r\n" % (a,AddSpace.add_space(a),element)]
        #                        #files3.writelines(element)
        #                        files3.writelines(sum)
        SortingWriteToFile.write_to_file(path_to_file_obwody, __table_count__)

        # print("Error 1 in genera_class I/O")
        return -1

        print("Oto efekt:")
        return 0
