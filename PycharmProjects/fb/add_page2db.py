import fb_getpage
import db
from pprint import pprint

#pages = ["DonaldTrump", "YairLapid","SivanRahavNews"]
pages = [ "YairLapid"]

fb = fb_getpage.Facebook()
mydb = db.DB()
for page_name in pages:
    mydb.add_posts(fb.get_posts(page_name))

pprint(mydb.get_posts())