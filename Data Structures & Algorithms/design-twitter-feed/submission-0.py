class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list) # # key: userId, val: [time, tweetId]
        self.follower = defaultdict(set) # key: followerId, val: list of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower[userId].add(userId) # include user themselves

        result = []
        heap = []
        for followeeId in self.follower[userId]:
            if followeeId in self.posts:
                i = len(self.posts[followeeId]) - 1 # the followee's most recent post
                time, tweetId = self.posts[followeeId][i]
                heap.append((time, tweetId, followeeId, i - 1))
        heapq.heapify(heap)
        
        while heap and len(result) < 10:
            time, tweetId, followeeId, i = heapq.heappop(heap)
            result.append(tweetId)
            if i >= 0:
                time, tweetId = self.posts[followeeId][i]
                heapq.heappush(heap, (time, tweetId, followeeId, i - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
