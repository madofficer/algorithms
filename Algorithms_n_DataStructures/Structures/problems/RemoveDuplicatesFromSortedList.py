# Definition for singly-linked list.
from typing import Optional

from Algorithms_n_DataStructures.Structures.LinkedList import LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:

                current_node = current_node.next

        return head

    def deleteDuplicates_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.next and head.val == head.next.val:
            head = head.next.next

        current_node = head
        temp = ListNode()
        temp.next = head
        prev = temp
        while current_node:

            if current_node.next and current_node.val == current_node.next.val:

                while current_node.next and current_node.val == current_node.next.val:
                    current_node = current_node.next

                prev.next = current_node.next

            else:
                prev = prev.next

            current_node = current_node.next

        return head


def list_to_linked_list(a: list):
    if not a:
        return None

    head = ListNode(a[0])
    curr_node = head
    for i in a[1:]:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next

    return head


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


print_list(Solution().deleteDuplicates_2(list_to_linked_list([1, 1, 1, 2, 3])))
