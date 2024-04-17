import csv
import logging

log = logging.getLogger(__name__)


class Line(object):
    def __init__(self):
        self._line = None

    def write(self, line):
        self._line = line

    def read(self):
        return self._line


def generate_report(data, list_columns, label_columns):
    line = Line()
    writer = csv.writer(line, delimiter=",")

    # header
    labels = []
    for key in list_columns:
        labels.append(label_columns[key])

    # rows
    writer.writerow(labels)
    yield line.read()

    for item in data:
        row = []
        for key in list_columns:
            value = getattr(item, key)
            # if value is a function, call it
            if callable(value):
                try:
                    row.append(str(value()))
                except Exception as e:
                    row.append("Error calling function")
            else:
                row.append(str(getattr(item, key)))
        writer.writerow(row)
        yield line.read()