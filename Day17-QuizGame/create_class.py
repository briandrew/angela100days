# create a class


class User:
    def __init__(self, user_id, username):  # must provide these 2 arguments when called
        print(f"creating user {username}.....")
        self.id = user_id
        self.username = username
        self.followers = 0  # set default ant not in requirements above
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# manually add attributes - like variables but for an object


user_1 = User("001", "Brian")
user_2 = User("002", "Niabi")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)









