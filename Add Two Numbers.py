# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode):
    num1 = ""
    num2 = ""
    while l1 is not None:
        num1 = str(l1.val) + num1
        l1 = l1.next
    while l2 is not None:
        num2 = str(l2.val) + num2
        l2 = l2.next

    sum = int(num1) + int(num2)
    ans = [None] * len(str(sum))
    for i, val in enumerate(reversed(str(sum))):
        ans[i] = ListNode(int(val))
    for i in range(len(ans) - 1):
        ans[i].next = ans[i + 1]

    return ans[0]


# Optimized solution from Leet Code
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
