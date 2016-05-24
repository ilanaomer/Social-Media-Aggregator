import fb_get_data
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


# pages = {'fan_count': 5, 'name': 'Donald J. Trump',
#          'fan_count': 3, 'name': 'Yair Lapid - יאיר לפיד',
#          'fan_count': 1, 'name': 'ccsd'}

#
@route('/fb/pages/')
def fb_pages_index():
    mydb = db.DB()
    pages = mydb.get_pages()
    return template('index_pages', pages=pages)

@route('/fb/posts/')
def fb_posts_index():
    mydb = db.DB()
    posts = mydb.get_posts()
    return template('index_posts', posts=posts)


@route('<path:path>')
def server_static(path):
    return static_file(path, root=r'static/fb')


if __name__ == "__main__":
    run(debug=True, reloader=True)
