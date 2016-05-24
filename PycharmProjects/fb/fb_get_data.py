import fb_auth
import facebook
from pprint import pprint


class Facebook:
    def __init__(self):
        self.TOKEN = fb_auth.get_fb_access().strip()
        self.graph = facebook.GraphAPI(access_token=self.TOKEN, version='2.5')

    def get_page(self, page_key):
        try:
            page = self.graph.get_object(page_key, fields="about,fan_count,name")
        except facebook.GraphAPIError:
            print("{}  - NO SUCH PAGE!!!".format(page_key))
            return None
        return page

    def get_posts(self, page_key):
        fb_posts = self.graph.get_object(page_key,
                                         fields="id,posts.limit(100){type,message,created_time, likes.summary(1)}")

        for fb_post in fb_posts['posts']['data']:
            if 'status' == (fb_post['type']):
                num_likes = fb_post['likes']['summary']['total_count']
                yield {
                    'post_id': fb_post['id'],
                    'created_time': fb_post['created_time'],
                    'message': fb_post['message'],
                    'num_likes': num_likes,
                    'page_id': fb_posts['id']}
