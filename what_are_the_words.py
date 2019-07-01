from general_class import GeneralClass
import operator


class GeneralClassWhatWor:
    print("***************start:********************")
    # __table_count__ = {"Ala":2,"Ola":3,"Jagoda":0,"Zygmunet":3," ":3}
    # sorted_d=sorted(__table_count__.items(),key=operator.itemgetter(1))
    # for k,v in sorted_d:
    #    sum = ["Count: %d Word: %r\n" % (v, k)]
    #    print(k,v)


if __name__ == '__main__':
    obiekt1 = GeneralClass
    obiekt1.read_metod_write('test_book', 'to_analy')
    print("***************the end*******************")
