import sys
import pprint

import facebook

from object import get_facebook_data
from pprint import pprint

sys.argv.append('g')
if __name__ == '__main__':
    pprint(get_facebook_data(sys.argv[1], 'posts'))

