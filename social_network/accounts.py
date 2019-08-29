
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline_posts_list =[]

        for user in self.following:
            timeline_posts_list += user.posts

        timeline_posts_list.sort(key=lambda x: x.timestamp)

        return timeline_posts_list

    def follow(self, other):
        self.following.append(other)

    def __str__(self):
        return 'User: "{} {}"'.format(self.first_name, self.last_name)
