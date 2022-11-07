class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            tail = ListNode(head.val)
            current = head.next
            while current:
                temp = current.next
                current.next = tail
                tail = current
            
                current = temp
            
            return tail
        except:
            return None
