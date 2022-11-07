class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        count = 1
        temp = head
        #counting the length of the linked list
        while temp:
            size += 1
            temp = temp.next
        #if the length is even go upto the n/2 th head
        if size % 2 == 0:
            while count <= size / 2:
                head = head.next
                count += 1
            return head
        #if the length is odd go upto the n//2 th head
        else:
            while count <= size // 2:
                head = head.next
                count += 1
            return head
