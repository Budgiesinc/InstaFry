import time
import os
from tempfile import gettempdir

from instapy import InstaPy

from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')

insta_username = 'jungusei'
insta_password = 'Qu3st10n'

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, headless_browser=False, password=insta_password,)
session.login()

# set up all the settings
# session.set_relationship_bounds(enabled=False,
# 				 potency_ratio=-1.21,
# 				  delimit_by_numbers=True,
# 				   max_followers=4590,
# 				    max_following=5555,
# 				     min_followers=45,
# 				      min_following=77)
session.set_user_interact(amount=4, randomize=True, percentage=50, media='Photo')
session.set_do_comment(True, percentage=20)
session.set_comments([u'Hit my Dm!', 'I miss stuff like this!!', 'Nicey!, I love the way this looks!'])

# session.set_dont_include(['friend1', 'friend2', 'friend3'])
# session.set_dont_like(['pizza', 'girl'])

session.follow_user_followers(['lilskies', 'laflare1017', 'liluzivert'], amount=30, randomize=True, interact=True, sleep_delay=600)
session.unfollow_users(amount=60, InstapyFollowed=(True, "all"), style="RANDOM", unfollow_after=90*60*60, sleep_delay=501)


# do the actual liking
session.like_by_tags(['hiphop', 'girl', 'art', 'rap'], amount=100)


# except Exception as exc:
#     # if changes to IG layout, upload the file to help us locate the change
#     if isinstance(exc, NoSuchElementException):
#         file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
#         with open(file_path, 'wb') as fp:
#             fp.write(session.browser.page_source.encode('utf8'))
#         print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
#             '*' * 70, file_path))
#     # full stacktrace when raising Github issue
#     raise

# finally:
    # end the bot session
session.end()
