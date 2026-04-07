class Twitter:

    def __init__(self):
        self.userIdToTweetIds = {}
        self.userIdToFolloweeIds = {}
        self.recentPosts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userIdToTweetIds:
            self.userIdToTweetIds[userId] = [tweetId]
        else:
            self.userIdToTweetIds[userId].insert(0, tweetId)
        self.recentPosts.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = len(self.recentPosts) - 1
        while len(res) < 10 and i >= 0:  
            tweet = self.recentPosts[i]
            if userId in self.userIdToFolloweeIds:
                for user in self.userIdToFolloweeIds[userId]:
                    if user in self.userIdToTweetIds and tweet in self.userIdToTweetIds[user]:
                        if tweet not in res:
                            res.append(tweet)
            if userId in self.userIdToTweetIds and tweet in self.userIdToTweetIds[userId] and tweet not in res:
                res.append(tweet)
            i -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userIdToFolloweeIds:
            self.userIdToFolloweeIds[followerId] = set([followeeId])
        else:
            self.userIdToFolloweeIds[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userIdToFolloweeIds:
            return
        elif followerId in self.userIdToFolloweeIds and followeeId in self.userIdToFolloweeIds[followerId]:
            self.userIdToFolloweeIds[followerId].remove(followeeId)
