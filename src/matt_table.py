"""
Create a table class that accepts:
    - numeric data in the form of a list of lists
    - a list of column names (strings)
This table should have the following methods:
    - select_rows(accepts a list of indices or list of bools)
    - select_cols(accepts a list of indicies or list of column names)
    - group_by(accepts a group by column, a second column and sum or mean)
"""


class Table:

    def __init__(self, data, cols):
        self.data = data
        self.cols = cols
        self._col_dict = dict(zip(cols, list(range(len(data[0])))))
        self._col_names = {v: k for k, v in self._col_dict.items()}

    def select_rows(self, rows):
        if type(rows[0]) == bool:
            rows_int = self._get_row_int(rows)
            return self._select_rows_int(rows_int)
        elif type(rows[0]) == int:
            return self._select_rows_int(rows)
        else:
            raise ValueError('Invalid row type')

    def _get_row_int(self, rows):
        rows_int = []
        for i, b in enumerate(rows):
            if b:
                rows_int.append(i)
        return rows_int

    def _select_rows_int(self, rows):
        temp = []
        for i in rows:
            temp.append(self.data[i])
        return Table(temp, self.cols)

    def select_cols(self, columns):
        if type(columns[0]) == str:
            col_int = self._get_col_int(columns)
            return self._select_cols_int(col_int)
        elif type(columns[0]) == int:
            return self._select_cols_int(columns)
        else:
            raise ValueError('Invalid column type')

    def _get_col_int(self, columns):
        return [self._col_dict[col_name] for col_name in columns]

    def _select_cols_int(self, columns):
        temp = []
        for row in self.data:
            temp_row = []
            for i in columns:
                temp_row.append(row[i])
            temp.append(temp_row)
            col_names = [self._col_names[n] for n in columns]
        return Table(temp, col_names)

    def group_by(self, col1, col2, agg):
        pass
