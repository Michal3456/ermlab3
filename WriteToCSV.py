# encoding: utf-8
# module WriteToCSV
# from ./WriteToCSV.py
# by written 2.00
# no doc

# imports
import csv
import re


# no Variables

# class


class WriteTiCSV:
    """
    open_file_count_word() -> bool.
    """

    # function

    @staticmethod
    def open_file_count_word(dict_words_quantity: dict) -> bool:  # real signature unknown; loaded from data/
        """
        open_file_count_word() -> bool

        Parameters
        -----------
        dict_words_quantity:
            Dictionary with words and number of the same words

        Returns
        -------
        return:
            Bool
        """
        try:
            csv.register_dialect('myDialect',
                                 quoting=csv.QUOTE_ALL,
                                 skipinitialspace=True)
            with open('words.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                for row in dict_words_quantity.items():
                    writer.writerow('d')
        except Exception as e:
            print("Error in write csv method: %e" % e)
            return False
        finally:
            f.close()
            return True

    @staticmethod
    def open_file_count_word(dict_words_quantity: [str]) -> bool:  # real signature unknown; loaded from data/
        """
        open_file_count_word() -> bool

        Parameters
        -----------
        dict_words_quantity:
            Dictionary with words and number of the same words

        Returns
        -------
        return:
            Bool
        """
        try:
            csv.register_dialect('myDialect',
                                 quoting=csv.QUOTE_ALL,
                                 skipinitialspace=True)
            with open('words.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                for row in dict_words_quantity:
                    writer.writerow(row)
        except Exception as e:
            print("Error in write csv method: %e" % e)
            return False
        finally:
            f.close()
            return True
