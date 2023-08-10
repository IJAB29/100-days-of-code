import requests


class Post:
    def getPosts(self, blog_url):
        blog_data = requests.get(blog_url).json()
        return blog_data
