# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1:ListNode, l2:ListNode):
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
    for i in range(len(ans)-1):
        ans[i].next = ans[i+1]
        
    return ans[0]