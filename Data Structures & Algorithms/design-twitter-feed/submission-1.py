from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set())
        self.tweets = defaultdict(list())
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        users = self.followMap[userId].copy()
        users.add(user_Id)

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
            
                heapq.heappush(heap, (-time, tweetId, user, index))
            
        while heap and len(result) < 10:
            time, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            if index > 0:
                index -= 1
                time, tweetId = selftweets[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
