class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) 
        candies = [1] * n

        # the logic is that if the next element needs more candies there is no problem because 
        # it does not affect anything in the previous elements, but if I need to update the previous element
        # then I need to fix all the previous ones; but only in the case where the relationship gets broken where the 
        # number of candies does not allow the conditions to be followed
        for i in range(1, n):
            if ratings[i - 1] == ratings[i]:
                continue
            elif ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] += (candies[i] - candies[i - 1]) + 1
                # for k in range(i - 1, 0, -1):
                #     if ratings[k - 1] > ratings[k] and candies[k - 1] <= candies[k]:
                #         candies[k - 1] += (candies[k] - candies[k - 1]) + 1
                #     else:
                #         break # this means the condition is followed, which also means that condition will be followed for all
                #         # the previous elements because nothing was broken as I am building the sequence from left to right correctly
            elif ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                candies[i] += (candies[i - 1] - candies[i]) + 1
        
        # it turns out there is no need to update anything inside the loop because I can run the loop backward and fix everything at once
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] += (candies[i] - candies[i - 1]) + 1
            
        return sum(candies)