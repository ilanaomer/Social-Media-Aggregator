import fb_getpage
import db
from bottle import route, run, template, static_file


# pages = ["DonaldTrump", "YairLapid","SivanRahavNews"]
# fb = fb_getpage.Facebook()
# mydb = db.DB()
# for page_name in pages:
#     page = fb.get_page(page_name)
#     mydb.add_page(page)
#
# mydb.get_pages()

# pages = []
# pages.append({'fan_count':5, 'name':'Donald J. Trump'})
# pages.append({'fan_count':3, 'name':'Yair Lapid - יאיר לפיד'})
# pages.append({'fan_count':1, 'name':'ccsd'})

@route('/fb')
def fb_index():
    mydb = db.DB()
    pages = mydb.get_pages()
    return template('index', pages=pages)


@route('<path:path>')
def server_static(path):
    return static_file(path, root=r'C:\Users\ilana\PycharmProjects\fb')


if __name__ == "__main__":
    run(debug=True, reloader=True)
    # !!!!
    # !!!!
