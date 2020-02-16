# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# l1: 2 -> 4 -> 3
# l2: 5 -> 6 -> 4

###
# The digits are stored in reverse order so
# the linked list l1 stores the number 342.
# We use this property to our advantage by doing the addition like it would have
# been done on pen and paper. We add the digits in reverse order and if there is
# carry, it will be added with the next set of digits. The benefit of this
# approach is that the result can be readily used to produce our output linked list.
###

class Solution:
    def addTwoNumbers(self,  l1: ListNode, l2: ListNode) -> ListNode:

        digit1 = l1
        digit2 = l2
        carry = 0

        dummyHead = ListNode(0)
        curr = dummyHead

        while( digit1 or digit2 ):
            if( digit1 ):
                num1 = digit1.val
                digit1 = digit1.next
            else:
                num1 = 0

            if( digit2 ):
                num2 = digit2.val
                digit2 = digit2.next
            else:
                num2 = 0

            total = num1 + num2 + carry
            if(total >= 10):
                curr.next = ListNode(total - 10)
                carry = 1
            else:
                curr.next = ListNode(total)
                carry = 0

            curr = curr.next

        if(carry == 1):
            curr.next = ListNode(1)

        return dummyHead.next
