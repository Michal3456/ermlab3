from Vector import Vector


class DelSymbols():
    @staticmethod
    def del_symbols(line2: Vector, line3: Vector):
        """Deleting special characters from the end of a word."""
        for word in line2:
            symbols = word[len(word) - 1]
            if symbols == ".":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "!":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "?":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "(":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == ")":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "#":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == ";":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == ",":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "-":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "\"":
                line3.append(word.replace(word[len(word) - 1], ''))
            elif symbols == "–":
                line3.append(word.replace(word[len(word) - 1], " "))
            elif symbols == '':
                line3.append(word.replace(word[len(word) - 1], " "))
            else:
                line3.append(word)
