
class User:
    def __init__(self, id: int, user_name: str):
        self.id = id
        self.user_name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User(1, "Tesla")
user_2 = User(2, "Newton")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
