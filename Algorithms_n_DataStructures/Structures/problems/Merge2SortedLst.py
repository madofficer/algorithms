from typing import Optional
from ListNode import ListNode, list_to_linked_list, print_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        elif list2:
            tail.next = list2

        return dummy_node.next



print_list(Solution().mergeTwoLists(list_to_linked_list([]), list_to_linked_list([0])))