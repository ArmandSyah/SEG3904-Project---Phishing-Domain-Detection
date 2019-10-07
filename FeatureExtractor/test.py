from URL.url import URL

u = URL('http://us.battle.net.ok.qqweb.asia/login/en/acc.htm')
import pprint
pprint.pprint(u.to_json())