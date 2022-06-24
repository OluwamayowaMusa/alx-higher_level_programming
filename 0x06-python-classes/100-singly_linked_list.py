#!/usr/bin/python3

""" A module which define Singly linked list.

"""


class Node:
    """ Defines the node of a singly linked list.

    """

    def __init__(self, data, next_node=None):
        """ Initializes the object with data and next_node.

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
        if not isinstance(value, (type(None), Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list.

    """

    def __init__(self):
        """ Initializes the Head node of a linked list.

        """
        self.__head = None
        """ Node: Head Node of linked list """

    def sorted_insert(self, value):
        """ Inserts a new node in the linked list """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            if temp.data > value:
                new_node.next_node = temp
                self.__head = new_node
                return
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            temp1 = temp.next_node
            temp.next_node = new_node
            new_node.next_node = temp1

    def __str__(self):
        """ String representation of linked list """
        _s = ''
        temp = self.__head
        while temp is not None:
            _s += (str(temp.data) + '\n')
            temp = temp.next_node
        return _s[:-1]
