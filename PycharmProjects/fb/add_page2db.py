import fb_get_data
import db
from pprint import pprint

#pages_names = ["DonaldTrump", "YairLapid","SivanRahavNews"]
pages_names = ["YairLapid"]

fb = fb_get_data.Facebook()
mydb = db.DB()

for page_name in pages_names:
    mydb.add_page(fb.get_page(page_name))
    mydb.add_posts(fb.get_posts(page_name))

    # pprint(fb.get_page(page_name)['name'])
    # for post in fb.get_posts(page_name):
    #     pprint(post['post_id'])
