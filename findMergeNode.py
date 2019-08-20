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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1 != curr2:
        if not curr1.next:
            curr1 = head2
        else:
            curr1 = curr1.next
        
        if not curr2.next:
            curr2 = head1
        else:
            curr2 = curr2.next
    return curr1.data

if __name__ == '__main__':
    index = 2
    llist1 = SinglyLinkedList()
    llist1_count = 3
    for llist1_item in [1,2,3]:
        llist1.insert_node(llist1_item)
        
    llist2_count = 1

    llist2 = SinglyLinkedList()

    for llist2_item in [1]:
        llist2.insert_node(llist2_item)
        
    ptr1 = llist1.head;
    ptr2 = llist2.head;

    for i in range(llist1_count):
        if i < index:
            ptr1 = ptr1.next
            
    while ptr2.next:
        ptr2 = ptr2.next

    ptr2.next = ptr1
    result = findMergeNode(llist1.head, llist2.head)
    print(result)