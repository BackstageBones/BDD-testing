from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"Class Blog initialized with params {self.title} for title, and {self.author} for author"

    def create_post(self, title, author):
        return self.posts.append(Post('Title', 'Test'))

    def json(self):
        pass
