class Solution:
    def __init__(self):
        self.result = None
        self.resultNodes = []
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = []
        temp = head
        temp2 = head
        #finding duplicates and storing them
        while temp:
            try:
                if temp.val == temp.next.val:
                    duplicates.append(temp.next.val)
                    temp = temp.next
                else:
                    temp = temp.next
            except:
                break 
                
        #creating the new linked list free of duplicates
        while head:
            if head.val in duplicates:
                head = head.next
            else:
                newNode = ListNode(head.val)
                if self.result == None:
                    self.result = newNode
                    self.resultNodes.append(self.result)
                else:
                    self.result.next = newNode
                    self.result = newNode
                head = head.next
        
        #return the new head
        if len(self.resultNodes):
            return self.resultNodes[0]
        else:
            return None
