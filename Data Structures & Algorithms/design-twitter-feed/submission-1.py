class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_time = {}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))
        self.tweet_time[self.count] = tweetId

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId]
        for follower in self.followers[userId]:
            feed = feed + self.tweets[follower]
        
        latest = []
        heapq.heapify(latest)
        for c, _ in feed:
            if len(latest) < 10:
                heapq.heappush(latest, c)
            elif c > latest[0]:
                heapq.heappop(latest)
                heapq.heappush(latest, c)

        latest_tweets = []
        while latest:
            latest_tweets.append(self.tweet_time[heapq.heappop(latest)])

        return latest_tweets[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
