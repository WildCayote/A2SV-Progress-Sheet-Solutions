class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if(len(people) == 1):
            return 1
        people.sort()
        boat = 0
        first=0
        last=len(people) - 1
        
        while(first<last):
            if((people[first] + people[last]) <= limit):
                boat += 1
                people[first] = 0
                people[last] = 0
                first += 1
                last -= 1
            else:
                last -= 1
        for i in range(len(people)):
            if(people[i]!= 0):
                boat += 1
        return boat
