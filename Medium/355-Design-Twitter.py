from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.store = {}
        self.time = 0

    def postTweet(self, userID: int, tweetID: int):
        if userID not in self.store:
            self.store[userID] = [set(), [], [], set()]
        self.store[userID][0].add(tweetID)
        self.store[userID][1].append([self.time, tweetID])
        for user in list(self.store[userID][3]):
            self.store[user][2].append([self.time, tweetID])
        self.time += 1
    
    def getNewsFeed(self, userID: int) -> List[int]:
        if userID not in self.store:
            return []
        heap = []
        for time, postID in self.store[userID][1]:
            heapq.heappush(heap, (-1*time, postID))
        for time, postID in self.store[userID][2]:
            heapq.heappush(heap, (-1*time, postID))
        ans = []
        while heap and len(ans) < 10:
            _, postID = heapq.heappop(heap)
            ans.append(postID)
        return ans
    
    def follow(self, followerID: int, followeeID: int):
        if followerID not in self.store:
            self.store[followerID] = [set(), [], [], set()]
        if followeeID not in self.store:
            self.store[followeeID] = [set(), [], [], set()]
        if followerID in self.store[followeeID][3]:
            return
        self.store[followeeID][3].add(followerID)
        if self.store[followeeID][1]:
            self.store[followerID][2] += self.store[followeeID][1]

    def unfollow(self, followerID: int, followeeID: int):
        if followerID not in self.store[followeeID][3]:
            return
        self.store[followeeID][3].remove(followerID)
        self.store[followerID][2] = [[time, tweetID] for time, tweetID in self.store[followerID][2] if tweetID not in self.store[followeeID][0]]