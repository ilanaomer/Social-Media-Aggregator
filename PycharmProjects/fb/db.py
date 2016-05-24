from pprint import pprint
import pymongo
import templates


# import dateutil.parser

# x = dateutil.parser.parse("2016-05-22T12:48:41+0000")
# pprint(x)

class DB:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.get_database('socialagg')
        self.pages_table = self.db.get_collection('pages')
        self.pages_table.create_index('id', unique=True)
        self.posts_table = self.db.get_collection('posts')
        self.posts_table.create_index('post_id', unique=True)
        self.posts_table.create_index('created_time')

    def add_page(self, page):
        self.pages_table.update({'id': page['id']}, page, upsert=True)

    def add_posts(self, posts):
        for post in posts:
            self.posts_table.update({'post_id': post['post_id']}, post, upsert=True)

    def get_posts(self):
        return self.posts_table.find()

    def get_pages(self):
        return self.pages_table.find()
        # pages = {page['id']: [page for page in pages.find()]

    # def get_pages_list(self):
    #     for page in self.pages_table.find():
    #         yield page
        # list += templates.ITEM_TEMPALTE.format(**page)
