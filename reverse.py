#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data), end=sep)
        node = node.next

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if not head:
        return head

    head.next, head.prev = head.prev, head.next

    if not head.prev:
        return head

    return reverse(head.prev)


if __name__ == '__main__':
    llist = DoublyLinkedList()

    for llist_item in [1,2,3,4]:
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1, ' ')
