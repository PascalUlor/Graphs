from random import random, shuffle
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.count = 0
        # !!!! IMPLEMENT ME

        # Add users

        # loop over a range of 0 to numUsers
        for i in range(0, numUsers):
            # add user to the graph
            self.addUser(f"User {i}")

        # Create friendships

        # Generate all friendship combinations
        # make a list of possible friendships
        possibleFreindships = []
        # avoid duplicates ensuring that the first number is smaller than the second
        
        # loop over userID in users
        for userID in self.users:
            # loop over friend id in a range from user id + 1 to the lastID +1
            for friendID in range(userID + 1, self.lastID + 1):
                # append the tuple of (user id , friend id) to the possible friendships list
                possibleFreindships.append((userID, friendID))
        # shuffle the possible friendships using the random.suffle method
        shuffle(possibleFreindships)
        # create afriendships of the first x ammount of pairs in the list   
        # X determined by the formula: numusers * avgFriendships // 2
        # we need to divide by to as each createFriendship adds 2 friendships
        # loop over a range to numUsers * avgFriendships // 2
        for i in range(numUsers * avgFriendships // 2):
            # set the friendship to possible friends at i
            friendship = possibleFreindships[i]
            # addfriendship of friendship[0] and friendship[1]
            self.addFriendship(friendship[0], friendship[1])
            self.count += 1
        print('=====',self.count)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            last_vertex = path[-1]
            if last_vertex not in visited:
                visited[last_vertex] = path
                for neighbour in self.friendships[last_vertex]:
                    # make a copy of the path
                    path_copy = list(path)
                    # append neighbour to the coppied path
                    path_copy.append(neighbour)
                    # then enqueue the copied path
                    q.enqueue(path_copy) 
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
