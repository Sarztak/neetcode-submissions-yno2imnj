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
        ids = [userId] + list(self.followMap[userId])
        tweets = []
        for i in ids:
            tweets.extend(self.tweetMap[i])
        tweets.sort(key=lambda x: x[0], reverse=True)

        topTen = tweets[:10]
        return [tweet_id for _, tweet_id in topTen]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.followMap[followerId]: 
                self.followMap[followerId].remove(followeeId)
