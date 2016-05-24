from pprint import pprint

import pymongo
import dateutil.parser

from object import GetFacebookData
get_fb = GetFacebookData()

# pages = ['Netanyahu', 'DonaldTrump', 'hillaryclinton']
# pages = ['Netanyahu']
#
#
# for p in pages:
#     pprint(get_fb.get_data(p, 'id,name,about,fan_count,posts'))

# pprint(get_facebook_data('Netanyahu', 'posts'))

client = pymongo.MongoClient()

db = client.get_database('socialagg')
# db = client['socialagg']

pages = db.get_collection('pages')
# pages = db['pages']

index_id = pages.create_index('id', unique=True)

# d = dateutil.parser.parse("2016-05-22T12:48:41+0000")
# print(d)
# pages.update({'id': "123456"},
#              {'id': '123456', 'name': 'Donald Duck', 'date': d},
#              upsert=True)

pages.update({'id': "123456"}, get_fb.get_data('Netanyahu', 'id,name,about,fan_count,posts'), upsert=True)

for page in pages.find():
    pprint(page.keys())

# pages.remove(index_id)
print("Done.")
