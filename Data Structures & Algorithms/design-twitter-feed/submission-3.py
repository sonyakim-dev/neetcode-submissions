class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list) # key: userId, val: [(tweetId, time)]
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        feed = []
        h = []

        for follow_id in self.follows[userId]:
            if follow_id in self.posts:
                i = len(self.posts[follow_id]) - 1
                tweet_id, time = self.posts[follow_id][i]
                h.append((time, tweet_id, follow_id, i-1))
        heapq.heapify(h)

        while h and len(feed) < 10:
            time, tweet_id, follow_id, i = heapq.heappop(h)
            feed.append(tweet_id)
            if i >=0:
                tweet_id, time = self.posts[follow_id][i]
                heapq.heappush(h, (time, tweet_id, follow_id, i-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
