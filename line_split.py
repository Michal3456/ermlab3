from add_word_to_dic import AddWord
from Vector import Vector
from del_symbols import DelSymbols


class LineSplit():
    def line_split(line: Vector, files: str, __table_count__: Vector, _table: Vector):
        """Division of lines into vector."""
        for line in files:
            line2 = line.split()
            line3 = []
            DelSymbols.del_symbols(line2, line3)
            AddWord.add_word_to_dic(line3, __table_count__, _table)
