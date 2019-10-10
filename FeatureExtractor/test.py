from URL.url import URL

u = URL('http://udn.com/news/story/7253/900738-Q1%E6%AF%8F%E8%82%A1%E6%90%8D%E7%9B%8A%EF%BC%8F%E7%9B%9F%E7%AB%8B+0.63%E5%85%83-%E5%85%AB%E5%AD%A3%E6%96%B0%E9%AB%98')
import pprint
pprint.pprint(u.to_json())