from Vector import Vector


class AddWord():
    @staticmethod
    def add_word_to_dic(line: Vector, __table_count__: Vector, _table: Vector):
        """Adding words to the dictionary and counting the occurrence of these words."""
        i = 0
        for word1 in line:

            if word1 not in _table:
                _table.append(word1)
                # print(_table[i])
                i = i + 1
                __table_count__[word1] = 1
            else:
                __table_count__[word1] = __table_count__[word1] + 1
            #    _table_count[word]=_table_count[word]+1
        i = 0
