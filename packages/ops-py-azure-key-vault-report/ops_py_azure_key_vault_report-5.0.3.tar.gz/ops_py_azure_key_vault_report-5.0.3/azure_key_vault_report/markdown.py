#!/usr/bin/env python


########################################################################################################################


class Markdown(object):
    """Creates a plain text Markdown table from a list (rows) of lists (columns). The header is the first list in the list.

    Attributes
    ----------
    rows : list
        The list of rows to make ut the table
    widths : dict
        A dict to store the column widths while parsing the columns for each row.

    Methods
    -------
    set_widths()
        Parses through the values of each column, in each row, in order to set the width of each column.
        Each column will have to be at least the size of the longest value in each column + an additional spacing.
    get_output(*args)
        Parses through each column in each row and adds the Markdown table char, the space and then the value.
        When the header row is done, the Markdown hyphen seperator row which separates the header and rows is added.
        The final result is returned
    """
    def __init__(self, rows):
        """
        Parameters
        ----------
        rows : list
            The list of rows to make ut the table.
        """
        self.rows = rows
        self.widths = {}

    def set_widths(self):
        """Parses through the values of each column, in each row, in order to set the width of each column."""

        for row in self.rows:
            for i, col in enumerate(row):
                cur_w = self.widths.get(i, 0)
                new_w = len(str(col).rstrip()) + 2
                if cur_w < new_w:
                    self.widths[i] = new_w

    def get_output(self, *args):
        """Parses through each column in each row and adds the Markdown table char, the space and then the value.

        Returns
        -------
        output : str
            The finalized table.

        """
        output = ""
        header_line = ""
        for n, row in enumerate(self.rows):
            for i, col in enumerate(row):
                value = f" {str(col).rstrip()} "

                if n == 0:
                    l = "-" * self.widths[i]
                    header_line += f"|{l: <{self.widths[i]}}"

                if n > 0 and i in args:
                    output += f"|{value: >{self.widths[i]}}"
                else:
                    output += f"|{value: <{self.widths[i]}}"

            output += "|\n"

            if header_line:
                output += f"{header_line}|\n"
                header_line = ""

        return output
