class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_time = {}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))
        self.tweet_time[self.count] = tweetId

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId]
        for follower in self.followers[userId]:
            feed = feed + self.tweets[follower]
        feed.sort(key = lambda x: x[0])
        latest_tweets = [tweet for _, tweet in feed[:10]]

        return latest_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
