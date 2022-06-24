#!/usr/bin/python3

""" A module which define Singly linked list.

"""


class Node:
    """ Defines the node of a singly linked list.

    """

    def __init__(self, data, next_node=None):
        """ Initilaizes the object with data and next_node.

        Args:
            data (int): Data in Node
            next_node (Node): Next node of linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets the data in Node. Checks for TypeError and
        raise Exception
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets the next node. Checks for if node is also a
        Node Object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, None, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list.

    """

    def __init__(self):
        """
