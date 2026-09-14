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
        result = []

        followers = self.followers[userId] | {userId}

        for user in followers:
            if self.posts[user]:
                index = len(self.posts[user]) - 1

                timestamp, tweetId = self.posts[user][index]
                heapq.heappush(max_heap, (-timestamp, tweetId, user, index))
        
        while max_heap and len(result) < 10:
            neg_time, tweet, user, index = heapq.heappop(max_heap)
            result.append(tweet)

            if index > 0:
                next_index = index - 1
                timestamp, tweetId = self.posts[user][next_index]
                heapq.heappush(max_heap, (-timestamp, tweetId, user, next_index))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
        
