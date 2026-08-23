from heapq import heapify, heappop, heappush
from collections import defaultdict
class Twitter:

    # maintain the heap of size 10.
    HEAP_SIZE = 10

    def __init__(self):
        # store my id and those that are following me
        self.followee_map = defaultdict(set)

        # store tweets by users 
        self.tweets_map = defaultdict(set)
        
        # store the k latest tweets on the heap. 
        # This is same as storing the k greatest numbers in 
        # the running stream of numbers.
        self.tweets_heap_map = {}

        # higher the timeId the more latest the tweet is.
        self.timeId = 0
        
    def _add_tweets_to_heap(self, uid, tweetId, timeId):
        # helper function to add tweets to the heap
        if uid in self.tweets_heap_map:
            heappush(self.tweets_heap_map[uid], (timeId, tweetId))
        else:
            self.tweets_heap_map[uid] = [(timeId, tweetId)]
            heapify(self.tweets_heap_map[uid])
        
        while len(self.tweets_heap_map[uid]) > self.HEAP_SIZE:
            heappop(self.tweets_heap_map[uid])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeId += 1
        if tweetId in self.tweets_map[userId]:
            raise Exception(f'{tweetId} already present')
        self.tweets_map[userId].add((self.timeId, tweetId))

        # the tweet needs to be added to two heap, one user's and another to the follower of the users, use a loop
        ids = set(uid for uid in self.followee_map[userId])
        ids.add(userId)
        for uid in ids:
            self._add_tweets_to_heap(uid, tweetId, self.timeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        self.timeId += 1
        if userId in self.tweets_heap_map:
            tweets = sorted(list(self.tweets_heap_map[userId]), reverse=True)
            return [t[1] for t in tweets]
        return []

    def follow(self, followerId: int, followeeId: int) -> None:
        self.timeId += 1
        if followeeId == followerId:
            # can't follow yourself
            return
        if followerId in self.followee_map[followeeId]:
            print(f'Already following {followeeId}')
        else:
            self.followee_map[followeeId].add(followerId)
            # also need to add the tweets to heap
            tweets = self.tweets_map[followeeId] # tweets of the one I am following
            for timeId, tweetId in tweets:
                self._add_tweets_to_heap(followerId, tweetId, timeId)
            print(f'Following {followeeId}')

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.timeId += 1
        if followeeId == followerId:
            # can't can't unfollow yourself
            return
        if followerId in self.followee_map[followeeId]:

            # remove the follower from the followee
            self.followee_map[followeeId].remove(followerId)

            # I need to recreate the heap once again after removing the tweets
            # I not only need to remove the tweets after unfollowing but also
            # need to add back my own tweets in case the heap size shrinks to
            # less that HEAP_SIZE and there is more space to add back my tweets

            tweets_to_remove = self.tweets_map[followeeId]
            tweets_to_add_back = self.tweets_map[followerId]
            tweets_feed = set(self.tweets_heap_map[followerId])

            # both are set, remove the common elements
            tweets_feed -= tweets_to_remove

            tweets_feed |= tweets_to_add_back

            # undo and redo make the heap 
            del self.tweets_heap_map[followerId]

            for timeId, tweetId in tweets_feed:
                self._add_tweets_to_heap(followerId, tweetId, timeId)
            print(f'Unfollowed {followeeId}')
        else:
            print(f'Not following {followeeId}')
        

