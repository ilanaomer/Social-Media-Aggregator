from pprint import pprint
import pymongo
#import dateutil.parser

#x = dateutil.parser.parse("2016-05-22T12:48:41+0000")
#pprint(x)

class DB:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.get_database('socialagg')
        self.pages_table = self.db.get_collection('pages')
        self.pages_table.create_index('id', unique=True)

    def add_page(self, page):
        self.pages_table.update( {'id': page['id']}, page, upsert=True)

    def get_pages(self):
        for page in self.pages_table.find():
            pprint(page)
        #pages = {page['id']: [page for page in pages.find()]
