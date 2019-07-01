# encoding: utf-8
# module RemoveStopWords
# from ./RemoveStopWords.py
# by written 1.00
# no doc

# imports
from nltk.corpus import stopwords

# Variable with simple values

_ERR = 0


# class


class RemoveStopWords:
    """
    remove_stop_words() ->[str].
    remove_stop_words(my_string_words) remove stop words from my_string_words.
    """

    # function
    @staticmethod
    def remove_stop_words(my_string_pos: [str]) -> [str]:
        """
        remove_stop_words remove stop words from my_string_pos

        :param my_string_pos:
        :return: [str]
        """
        list22 = []
        for row in my_string_pos:
            if not row.isdigit() and not (row in stopwords.words('polish')):
                list22.append(row)
        return list22
