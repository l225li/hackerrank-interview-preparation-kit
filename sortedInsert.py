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

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    
    node = DoublyLinkedListNode(data)

    if not head:
        head = node
        return head
    
    curr = head

    while curr.next and curr.data <= data:
        curr = curr.next

    if curr.data > data:
        node.prev, node.next = curr.prev, curr
        if curr.prev:
            curr.prev.next = node
        else:
            head = node
    else:
        curr.next, node.prev = node, curr

    return head

            

if __name__ == '__main__':
    llist = DoublyLinkedList()

    for llist_item in [3, 6, 7, 18]:
        llist.insert_node(llist_item)

    data = 1

    llist1 = sortedInsert(llist.head, data)

    print_doubly_linked_list(llist1, ' ')