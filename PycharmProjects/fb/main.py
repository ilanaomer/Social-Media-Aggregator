import fb_getpage
import db
from pprint import pprint

pages = ["DonaldTrump", "YairLapid","SivanRahavNews"]
fb = fb_getpage.Facebook()
mydb = db.DB()
for page_name in pages:
    page = fb.get_page(page_name)
    mydb.add_page(page)

mydb.get_pages()
