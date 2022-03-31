
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head):
        pre = None
        cur = head
        while cur:
            nextcode = cur.next
            cur.next = pre
            pre = cur
            cur = nextcode
        return pre

#删除单链表某一节点  leet code 237
class Solution:
    def deleteNode(self, node):
        next_code = node.next
        next_next_code = node.next.next
        node.val = next_code.val
        node.next = node.next.next


#合并两个有序的链表 leetcode 21

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(None)
        cur = root
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            cur.next = node
            cur = node
        cur.next = list1 or list2
        return root.next