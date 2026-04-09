class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) 
        candies = [1] * n

        for i in range(1, n):
            if ratings[i - 1] == ratings[i]:
                continue
            elif ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] += (candies[i] - candies[i - 1]) + 1
                for k in range(i - 1, 0, -1):
                    if ratings[k - 1] > ratings[k] and candies[k - 1] <= candies[k]:
                        candies[k - 1] += (candies[k] - candies[k - 1]) + 1
            elif ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                candies[i] += (candies[i - 1] - candies[i]) + 1
        
        return sum(candies)