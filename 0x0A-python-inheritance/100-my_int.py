#!/usr/bin/python3
""" Defines a class that inherits from int.

"""


class MyInt(int):
    """ A class that inherits from int.

    """

    def __eq__(self, other):
        """ Inverts the == operator.

        Args:
            other (int): Operand
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Inverts the != operator.

        Args:
            other (int): Operand
        """
        return not super().__ne__(other)
