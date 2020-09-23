#!/usr/bin/python3
""" This module creates a class Node"""


class Node:
    """Node class that represents a node

    Attributes:
        __data (int): data
        __next_node (Node): node
    """
    def __init__(self, data=0, next_node=None):
        """Initializes a node

        Args:
            data (int): data
            next_node (Node): node

        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data

        Returns:
            Value of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data

        Args:
            value (int): value for data

        Returns:
            None

        Raises:
            TypeError: if type(data) is not int
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter for next_node

        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_nodeSinglyLinkedList

        Args:
            value (Node): next node

        Returns:
            None

        Raises:
            TypeError: if type(value) is not Node and value is not None
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class that represents a singly linked list

    Attributes:
        __head (Node): head of the list
    """

    def __init__(self):
        """Initializes a linked list

        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): data for the new Node

        Returns:
            None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            new.next_node = tmp
            self.__head = new
        else:
            while tmp.next_node is not None:
                if tmp.next_node.data >= value:
                    break
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Prints the linked list

        Returns:
            None
        """
        string = ""
        tmp = self.__head
        while tmp:
            string += str(tmp.data)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
