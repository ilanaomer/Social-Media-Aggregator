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
            page['posts'] = self.get_posts(page_key)
        except facebook.GraphAPIError:
            print("{}  - NO SUCH PAGE!!!".format(page_key))
            return None
        return page

    def get_posts(self, page_key):
        posts = {}
        fb_posts = self.graph.get_object(page_key, fields="posts.limit(100){type,message,created_time}")
        for fb_post in fb_posts['posts']['data']:
            if 'status' == (fb_post['type']):
                num_likes = self.get_num_likes(fb_post['id'])
                posts[fb_post['id']] = [fb_post['created_time'], fb_post['message'], num_likes]
        return posts

    def get_num_likes(self, item_id):
        args = {}
        args["summary"]=1
        o = self.graph.request(  item_id + '/likes', args)
        return o['summary']['total_count']
        return o