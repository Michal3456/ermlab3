from is_it_word import IsWord
from add_space import AddSpace
class GeneralClass:
    def read_metod(path_to_file_book: str, path_to_file_obwody: str):
                '''DESCRIPTION'''
                with open(path_to_file_book) as files:
                    _table = []
                    _table_count = {}
                    cos = "cos"
                    i =0
                    for line in files:
                        line2 = line.split()
                        # for count, elem in enumerate(line2):
                        #    print(count, elem)
                        #print(line2)
                        for word in line2:
                            if word not in _table:
                                _table.append(word)
                                #print(_table[i])
                                i=i+1
                                _table_count[word]=1
                            else:
                                _table_count[word]=_table_count[word]+1
                            #    _table_count[word]=_table_count[word]+1
                i=0
                #for element in _table:
                #    print(element)
                with open(path_to_file_obwody, 'a') as files3:
                        for element in _table_count:
                            #print(element)
                            #print(_table_count[element])
                            a=_table_count[element]
                            sum = ["Ilość: %d %s Słowo: %r\n" % (a,AddSpace.add_space(a),element)]
                            #files3.writelines(element)
                            files3.writelines(sum)

                #print("Error 1 in genera_class I/O")
                return -1

                print("Oto efekt:")
                return 0


