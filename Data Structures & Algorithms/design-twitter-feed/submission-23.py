from heapq import merge
from collections import defaultdict
class Twitter:
    def __init__(self) -> None:
        self.timer = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1
    def getNewsFeed(self, userId) -> list:
        user_ids = self.following[userId] | {userId}
        # merge expect the lists to be sorted in ascending order, but they are not, so reversed is needed.
        # reads are rare relative to writes in Twitter's model, so paying the cost at read time is better.
        all_users_tweets = [reversed(self.tweets[uid]) for uid in user_ids if uid in self.tweets]
        results = []
        for timer, tweetId in merge(*all_users_tweets):
            results.append(tweetId)
            if len(results) == 10:
                break
        return results
    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
