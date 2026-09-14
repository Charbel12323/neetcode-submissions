class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # We first need to get all the followers for this user
        # for each of there followers, we must get all there posts
        # put them in a max_heap

        max_heap = []
        heapq.heapify(max_heap)

        for timestamp, post in self.posts[userId]:
            heapq.heappush(max_heap, (-timestamp, post))
        
        for followeeId in self.followers[userId]:
            for timestamp, post in self.posts[followeeId]:
                heapq.heappush(max_heap, (-timestamp, post))
        
        result = []

        while max_heap and len(result) < 10:
            timestamp, tweetId = heapq.heappop(max_heap)
            result.append(tweetId)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
        
