#!/bin/python3


class StringCalulator:
    def sum(self, num=None):
        try:
            _delimiter = ","
            if num.startswith("//"):
                _delimiter = num[2]
                num = num[3:]
            negatives = [i for i in num.split(_delimiter) if "-" in i]
            if negatives:
                return f"negatives not allowed: {' '.join(negatives)}"
            _thousands = [i for i in num.split(_delimiter) if int(i) > 1000]
            if _thousands:
                num = [i for i in num.split(_delimiter) if int(i) < 1000]
            if num:
                _split = "".join(num).split(_delimiter)
                return sum(map(int, _split))
            else:
                return 0
        except AttributeError:
            return 0
