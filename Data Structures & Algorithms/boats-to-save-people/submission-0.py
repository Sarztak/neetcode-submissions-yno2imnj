class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        i, j = 0, len(people) - 1
        people = sorted(people)
        while i <= j:
            if i == j or people[j] == limit:
                # this is the case where only one person can be fit into the
                # boat because of capactity constrains or else beause I just have one person left
                j -= 1
            elif people[i] + people[j] <= limit:
                # this is case where the boat can carry two people
                j -= 1
                i += 1
            else:
                # this is the case when boat cannot fit two people, so only the heavier person is carried
                # since the series is sorted that will be person at jth index
                j -= 1
            
            count += 1 # in each case the boat will not be empty so count is increased
        
        return count
        