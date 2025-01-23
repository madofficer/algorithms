from typing import Optional

from ListNode import ListNode, list_to_linked_list, print_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        def addNode(data):
            nonlocal dummy_node
            new_node = ListNode(data)
            if dummy_node is None:
                dummy_node = new_node
                return
            else:
                current_node = dummy_node
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = new_node
        over_digit = 0
        while l1 and l2:
            curr_sum = l1.val + l2.val + over_digit
            digit = curr_sum % 10
            over_digit = curr_sum // 10
            addNode(digit)
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_sum = l1.val + over_digit
            digit = curr_sum % 10
            over_digit = curr_sum // 10
            addNode(digit)
            l1 = l1.next

        while l2:
            curr_sum = l2.val + over_digit
            digit = curr_sum % 10
            over_digit = curr_sum // 10
            addNode(digit)
            l2 = l2.next

        if over_digit != 0:
            addNode(over_digit)


        return dummy_node.next


print_list(Solution().addTwoNumbers(list_to_linked_list([0, 1]), list_to_linked_list([0])))

