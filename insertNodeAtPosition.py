#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end=sep)
        node = node.next

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        return head
    curr = head
    while position > 1 and curr.next:
        curr = curr.next
        position -= 1
    
    node.next, curr.next = curr.next, node
    return head


if __name__ == '__main__':

    llist_count = 3
    llist = SinglyLinkedList()

    for llist_item in [16, 13, 7]:
        llist.insert_node(llist_item)

    data = 1
    position = 2
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, ' ')

