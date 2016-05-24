from pprint import pprint
import facebook


class GetFacebookData:

    def __init__(self):
        with open(r'C:\Users\Menahem\PycharmProjects\facebook_requests\TOKEN.txt') as f:
            self.TOKEN = f.read().strip()
            self.graph = facebook.GraphAPI(access_token=self.TOKEN, version='2.5')

    def get_data(self, profile_name, data_type):
        if not profile_name:
            pprint("Profile facebook name is required!")
            return None
        try:
            o = self.graph.get_object("{}?fields={}".format(profile_name, data_type))
        except facebook.GraphAPIError:
            pprint("Page not found!")
            return None
            o = self.graph.get_object("{}?fields={}".format(profile_name, data_type))

        # pprint(o)
        return o

# pprint(get_facebook_data('DonaldTrump','posts'))
# pprint(get_facebook_data('Netanyahu','posts'))
