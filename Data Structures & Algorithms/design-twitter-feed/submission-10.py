from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = list(self.followMap[userId])
        ids.append(userId)
        tweets = []
        heapq.heapify(tweets)
        for i in ids:
            for tweet in self.tweetMap[i]:
                if len(tweets) < 10:
                    heapq.heappush(tweets, tweet)
                else:
                    if tweets[-1][0] < tweet[0]:
                        heapq.heappop(tweets)
                        heapq.heappush(tweets, tweet)

        tweets.sort(reverse=True)
        return [tweet_id for _, tweet_id in tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.followMap[followerId]: 
                self.followMap[followerId].remove(followeeId)
